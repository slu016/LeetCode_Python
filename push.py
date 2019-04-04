import os
import subprocess

git = "C:/Program Files/Git/cmd/git.exe"
git_add = '"%s" add *'%git
git_commit = '"%s" commit -m "test"'%git
git_push = '"%s" push'%git


# print(os.getcwd())

# 获取当前文件路径
current_path = os.path.abspath(__file__)
# 获取当前文件的父目录
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

os.chdir(father_path)
# print(os.getcwd())
# print(git_add)
# os.system(git_add)
# os.system(git_commit)
# os.system(git_push)
# 用上面的会有路径空格问题

# os.popen(git_add)
# os.popen(git_commit)
# os.popen(git_push)

ps1 = subprocess.Popen(git_add) # 执行cmd命令
ps1.wait()#让程序阻塞
ps2 = subprocess.Popen(git_commit)
ps2.wait()
ps3 = subprocess.Popen(git_push)
ps3.wait()
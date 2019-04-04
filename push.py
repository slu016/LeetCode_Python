import os

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
print(os.getcwd())
# os.system(git_add)
# os.system(git_commit)
# os.system(git_push)

os.popen(git_add)
os.popen(git_commit)
os.popen(git_push)
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.



Example:

Input: "cbbd"

Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        if s is None:
            return ''
        ret = ''
        lens = len(s)
        max = 0
        dp = [[0] * lens for i in range(lens)] #产生一个lens*lens全0二维数组，dp数组后面存储True或False
        for j in range(lens):
            for i in range(j + 1): #双重循环可理解为以构造i开头j结尾的串
                dp[i][j] = (( s[i] == s[j] ) and (j - i <= 2 or dp[i + 1][j - 1])) #如果s[i]=s[j]说明串的首尾相同，并且j-i为0表示只有一个字符必为回文，j-i=1两个字符切相等必为回文，j-i=2三个字符首尾相同无论中间是什么必为回文，或者dp[i + 1][j - 1]为真表示去掉首尾为回文，而新加的首尾相同必为回文
                if dp[i][j] and j - i + 1 > max:
                    max = j - i + 1
                    ret = s[i:j + 1] #表示i开头j结束的串回文并且最长则更新长度max和回文串ret
        return ret

print(Solution().longestPalindrome('bababd'))
print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('cbbd'))
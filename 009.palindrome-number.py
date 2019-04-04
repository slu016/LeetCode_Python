'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:

Could negative integers be palindromes? (ie, -1) 负数都不是回文数

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

#转换成字符串的:
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num=0
        if(x<0):
            return False
        if int(str(x)) == int(str(x)[::-1]):
            return True
        return False

#不转换成字符串的：
class Solution2:
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num=0
        temp=x
        if x<0: return False
        while x!=0:
            num=num*10+x%10
            x=x//10
        if temp==num:
            return True

if __name__ == '__main__':
    result = Solution().isPalindrome(1) #0-9是回文数
    result2 = Solution2().isPalindrome2(1234321)
    print(result)
    print(result2)
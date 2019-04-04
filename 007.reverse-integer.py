'''
Reverse digits of an integer.


Example1: x =  123, return  321
Example2: x = -123, return -321


click to show spoilers.

Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if (x < 0):
            y = -1 * int((str(-x))[::-1])  # 由于最后我们在进行逆序操作后，返回值为整型，因此会有将字符型转化为整形的操作，经过编译，可以发现int()函数自动将前面多余的0给删去了，因此不需要考虑如何去除前面的0。
        else:
            y = int((str(x))[::-1])
        if (y > (2 ** 32 / 2 - 1) or y < (-(2 ** 32 / 2))):
            y = 0
        return (y)

if __name__ == '__main__':
    sd = 'qwerty'
    print(sd[::-1])
    result = Solution().reverse(-120)
    print(result)
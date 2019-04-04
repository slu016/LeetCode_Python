'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strLen = len(str)
        if str == '':
            return 0
        i = 0

        while (i < strLen):
            # 跳过空白字符
            if (str[i] == ' '):
                i += 1
            else:
                break

        if i == strLen:
            return 0
        signal = 1
        if str[i] == '+':
            signal = 1
            i += 1
        elif str[i] == '-':
            signal = -1
            i += 1

        res = 0
        # Python不声明变量类型，数字超出int型范围自动转为长整型，因此要在80000000前加负号
        maxInt = 0x7FFFFFFF
        minInt = -0x80000000

        while (i < strLen):
            if ((str[i] >= '0') & (str[i] <= '9')):
                # 是数字则乘以权值并相加
                res = res * 10 + signal * (int(str[i]))
            else:
                return res
            # 这里可加语句用来调试print 'str[%d]=%s,res=%d'%(i,str[i],res)
            if (res > maxInt):
                return maxInt
            elif (res < minInt):
                return minInt
            i += 1;

        return res


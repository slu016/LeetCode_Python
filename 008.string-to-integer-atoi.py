'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

import operator
import re

class Solution:
    def atoi(self, str):
        str = str.strip() #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。rstrip() 删除 string 字符串末尾的指定字符（默认为空格）。lstrip() 方法用于截掉字符串左边的空格或指定字符。
        flag = 1
        result=0
        i=0
        if operator.eq(str, "") == True or len(str) == 0:
            return 0
        if str [0]=='-':
            flag =-1
            i=i+1
        elif str[0]=='+':
            i=i+1
        while(i<len(str)):
            if not str[i].isdigit(): # isdigit() 方法检测字符串是否只由数字组成
                break
            else:
                result = result *10 +int(str[i])
            i=i+1
        if flag*result >  2147483647:
            return   2147483647
        if flag*result <  -2147483648:
            return -2147483648
        return flag*result


class Solution2:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str = re.findall('^[\+\-0]*\d+', str) #str是个列表，int()不能作用在列表上
        result = int(str[0]) #把列表的第一个元素-字符串取出来，转换成数字
        if result > 2147483647:
            return 2147483647
        if  result < -2147483648:
            return -2147483648
        return  result


if __name__ == '__main__':
    result = Solution().atoi('+323bce67')
    result2 = Solution2().atoi('-33aec67')
    print(result)
    print(result2)
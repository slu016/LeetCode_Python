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

class Solution:
    def atoi(self, str):
        str = str.strip()
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
            if not str[i].isdigit():
                break
            else:
                result = result *10 +int(str[i])
            i=i+1
        if flag*result >  2147483647:
            return   2147483647
        if flag*result <  -2147483648:
            return -2147483648
        return flag*result

if __name__ == '__main__':
    result = Solution().atoi('33')
    print(result)
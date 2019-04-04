'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R


And then read line by line: "PAHNAPLSIIGYIR"


Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        消耗numRows是5，我们看到这样的锯齿形图案：(here Algorithmic thinking)

        我们可以看到数字0~7在这里是一个小模式，如果我们除以8，我们可以在其他小模式中获得相同的数字。如
        0％8 = 0; 8％8 = 0
        1％8 = 1; 9％8 = 1
        所以我们可以使用此功能并将它们过滤到我们存储的行中。

        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        t = (numRows - 1) * 2  #t是竖行的下标周期
        for i, item in enumerate(s):
            if i % t >= numRows:
                rows[(t - i % t)] += item #存放斜行的结果
            else:
                rows[i % t] += item #存放竖行的结果
        return ''.join(rows) #把每一行的结果前后连接在一起


if __name__ == '__main__':
    string = '0123456789'
    result = Solution().convert(string, 3)
    print(result)
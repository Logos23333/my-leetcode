class Solution:
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        l = [""]*numRows
        direction = 1  # 1 represents down, -1 represents up
        index = -1  # represent which string to be selected
        for i in range(len(s)):
            index = index+direction
            l[index] += s[i]

            if i % (numRows-1) == 0 and i != 0:  # revert the direction
                direction = (-1)*direction

        ret = ""
        for i in range(numRows):
            ret += l[i]
        return ret

'''
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''
'''
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
'''
input1 = "PAYPALISHIRING"
numRows1 = 3

input2 = "PAYPALISHIRING"
numRows2 = 4

solution = Solution()
print(solution.convert(input1, numRows1))
print(solution.convert(input2, numRows2))

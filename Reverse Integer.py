class Solution:
    def reverse(self, x):
        if x == 0:
            return 0
        s = str(x)
        s = s.lstrip('-')

        s = s[::-1]
        s = s.lstrip('0')
        if x < 0:
            s = '-'+s

        ret = int(s)

        if ret > 2147483647 or ret < -2147483648:
            return 0
        else:
            return ret


'''
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''

solution = Solution()
input1 = 123
input2 = -123
input3 = 120
print(solution.reverse(input1))
print(solution.reverse(input2))
print(solution.reverse(input3))
print(solution.reverse(1534236469))

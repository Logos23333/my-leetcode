class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        s = str(x)
        s.lstrip('-')
        return s == s[::-1]

    def isPalindrome_withoutstr(self, x):  # incomplete
        if x < 0:
            return False

        copy = x
        revert = 0
        while copy > 0:
            revert = revert*10+copy/10
            copy /= 10

        print(revert)
        return revert == x


'''
example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
input1 = 121
input2 = -121
input3 = 10
solution = Solution()

print(solution.isPalindrome(input1))
print(solution.isPalindrome(input2))
print(solution.isPalindrome(input3))

print(solution.isPalindrome_withoutstr(input1))
print(solution.isPalindrome_withoutstr(input2))
print(solution.isPalindrome_withoutstr(input3))

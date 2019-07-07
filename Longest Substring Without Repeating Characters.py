class Solution:
    def lengthOfLongestSubstring(self, s):
        result = 0
        length = len(s)
        a = set()
        i = 0
        j = 0

        while (i < length) & (j < length):
            if s[j] not in a:
                a.add(s[j])
                j = j+1
                result = max(result, j-i)
            else:
                a.remove(s[i])
                i = i+1

        return result


'''
expected output:
"abc", 3
'''
input1 = "abcabcbb"

'''
expected output:
"b", 1
'''
input2 = "bbbbb"

'''
expected output:
"wke", 3
'''
input3 = "pwwkew"

'''
expected output:
"abc", 3
'''
input4 = "abcabcbb"

input5 = "tmmzuxt"

solution = Solution()
print(solution.lengthOfLongestSubstring(input1))
print(solution.lengthOfLongestSubstring(input2))
print(solution.lengthOfLongestSubstring(input3))
# print(solution.lengthOfLongestSubstring_dict(input4))
# print(solution.lengthOfLongestSubstring_dict(input5))

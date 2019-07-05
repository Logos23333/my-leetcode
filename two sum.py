""" one-pass version & two-pass version"""
"""  注意两个版本返回list时其元素顺序不同，why?"""


class Solution:
    def twoSum_onepass(self, nums, target):
        hashmap = {}
        for i, value in enumerate(nums):
            find = target-value
            if find not in hashmap:
                hashmap[value] = i
            else:
                return [hashmap[find], i]

    def twoSum_twopass(self, nums, target):
        hashmap = {}
        for i, value in enumerate(nums):
            hashmap[value] = i

        for i in range(len(nums)):
            complement = target-nums[i]
            if((complement in hashmap) & hashmap[complement] != i):
                return [i,hashmap[complement]]


nums = [7, 2, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum_onepass(nums, target))
print(solution.twoSum_twopass(nums, target))

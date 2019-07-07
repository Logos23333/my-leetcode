class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        count = 0
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1+len2
        target = length/2
        flag = 0
        if (length % 2) == 1:
            flag = 1
        else if (length % 2) == 0:
            flag = 0

        i1 = 0
        i2 = 0
        while count != target:
            if i1 >= len1:

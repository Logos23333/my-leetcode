class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        count = 0
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1+len2
        target = (int)(length/2)

        i1 = 0
        i2 = 0

        l = list()
        while count <= target:
            if i1 >= len1:
                l.append(nums2[i2])
                i2 = i2+1
                count = count+1
                continue

            if i2 >= len2:
                l.append(nums1[i1])
                i1 = i1+1
                count = count+1
                continue

            if nums1[i1] >= nums2[i2]:
                l.append(nums2[i2])
                i2 = i2+1
            else:
                l.append(nums1[i1])
                i1 = i1+1

            count = count+1

        if (length % 2) == 1:
            return l[target]
        else:
            return (l[target-1]+l[target])/2


solution = Solution()

nums1 = []
nums2 = [4]

print(solution.findMedianSortedArrays(nums1, nums2))

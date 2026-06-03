class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1+nums2
        n = len(nums3)
        nums3.sort()

        if n % 2 != 0:
            median = nums3[(n-1)//2]

        else:
            midsum = nums3[n//2] + nums3[n//2-1]
            median = midsum/2
        return float(median)
        
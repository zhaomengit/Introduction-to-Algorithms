"""
详细思路见: https://discuss.leetcode.com/category/12/median-of-two-sorted-arrays
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        size1 = len(nums1)
        size2 = len(nums2)

        if size1 < size2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = size2 * 2
        l1 = 0.0
        l2 = 0.0

        while low <= high:
            mid2 = int((low + high) / 2)
            mid1 = size1 + size2 - mid2

            if mid1 == 0:
                l1 = float("-Infinity")
            else:
                l1 = float(nums1[int((mid1 - 1) / 2)])

            if mid1 == size1 * 2:
                r1 = float("Infinity")
            else:
                r1 = float(nums1[int(mid1 / 2)])

            if mid2 == 0:
                l2 = float("-Infinity")
            else:
                l2 = nums2[int((mid2 - 1) / 2)]

            if mid2 == size2 * 2:
                r2 = float("Infinity")
            else:
                r2 = nums2[int(mid2 / 2)]

            if l1 > r2:
                low = mid2 + 1
            elif l2 > r1:
                high = mid2 - 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2

        return -1

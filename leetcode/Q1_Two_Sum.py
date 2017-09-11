"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].

解题思路:通过dict存储对应target和每个元素的差量来遍历元素
"""

from collections import defaultdict
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_s = defaultdict()
        for i in range(len(nums)):
            if nums[i] not in dict_s:
                dict_s[target - nums[i]] = i
            else:
                return [dict_s[nums[i]], i]
        return [None, None]


s = Solution()
print(s.twoSum([2, 7, 8, 9, 5], 15))

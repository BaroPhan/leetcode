#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        for (index, value) in enumerate(nums):
            max = value
            for j in range(index+1, len(nums)):
                if nums[j] > nums[j-1]:
                    max += nums[j]
                else: break
            if max > max_sum: max_sum = max
        return max_sum
        
# @lc code=end



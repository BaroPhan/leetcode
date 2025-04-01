#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
import enum
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        track_min = nums[0]
        track_max = nums[0]
        min_value = nums[0]
        max_value = nums[0]
        for i in range(1, len(nums)):
            track_max = max(track_max + nums[i], nums[i])
            max_value = max(max_value, track_max)
            track_min = min(track_min + nums[i], nums[i])
            min_value = min(min_value, track_min)
        return max(abs(min_value), max_value)


# @lc code=end

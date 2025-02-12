#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_value = -1
        dict = {}
        for index, value in enumerate(nums):
            sum_value = sum(int(i) for i in str(value))
            if sum_value not in dict:
                dict[sum_value] = value
            else:
                if max_value < dict[sum_value] + value:
                    max_value =  dict[sum_value] + value
                dict[sum_value] =  max(dict[sum_value], value)
        return max_value


# @lc code=end
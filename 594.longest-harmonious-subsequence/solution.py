"""
594. Longest Harmonious Subsequence
https://leetcode.com/problems/longest-harmonious-subsequence
Solved
Easy
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.



Constraints:
1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
"""

from typing import Counter, List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_counter = dict(sorted(counter.items()))
        n = len(sorted_counter)
        lhs = 0
        keys = list(sorted_counter.keys())
        for i in range(1, n):
            prev_key = keys[i-1]
            curr_key = keys[i]
            if curr_key - prev_key == 1:
                prev_val = sorted_counter[prev_key]
                curr_val = sorted_counter[curr_key]
                lhs = max(lhs, curr_val + prev_val)
        return lhs

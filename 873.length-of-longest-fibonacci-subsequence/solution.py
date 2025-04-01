#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Store array elements in set for O(1) lookup
        num_set = set(arr)
        max_len = 0
        n = len(arr)

        # Try all possible first two numbers of sequence
        for start in range(n):
            for next in range(start + 1, n):
                # Start with first two numbers
                prev = arr[next]
                curr = arr[start] + arr[next]
                curr_len = 2

                # Keep finding next Fibonacci number
                while curr in num_set:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    max_len = max(max_len, curr_len)

        return max_len  


# @lc code=end
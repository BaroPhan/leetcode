"""
368. Largest Divisible Subset
https://leetcode.com/problems/largest-divisible-subset
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""


from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        f = [1] * n
        k = 0
        for i in range(n):
            for j in range(i):
                # print(f'i: {i}, j: {j}')
                if nums[i] % nums[j] == 0:
                    f[i] = max(f[i], f[j] + 1)
                if f[k] < f[i]:
                    k = i
                # print(f'k: {k}, f: {f}')
                # print('======================')

        m = f[k]
        i = k
        ans = []
        while m:
            # print(ans, k, i)
            if nums[k] % nums[i] == 0 and f[i] == m:
                ans.append(nums[i])
                k, m = i, m - 1
            i -= 1
        # print(ans)
        return ans

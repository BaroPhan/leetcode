"""
2537. Count the Number of Good Subarrays
https://leetcode.com/problems/count-the-number-of-good-subarrays
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.


Constraints:
1 <= nums.length <= 105
1 <= nums[i], k <= 109
"""


from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        good_subarr = 0
        l = 0
        num_hash = {}
        pair_count = 0

        if len(nums) < 2:
            return 0
        # print('nums: ', nums)

        for r in range(n):
            r_num = nums[r]
            if r_num not in num_hash:
                num_hash[r_num] = [1, 0]
            else:
                num_hash[r_num][0] += 1
                pair_count -= num_hash[r_num][1]
                num_hash[r_num][1] = (
                    num_hash[r_num][0] * (num_hash[r_num][0] - 1)
                ) // 2
                pair_count += num_hash[r_num][1]
            # print('num_hash: ', num_hash)
            # print('pair_count: ' , pair_count)

            while pair_count >= k and l <= r:
                # print('l: ', l)
                good_subarr += n - r
                l_num = nums[l]
                pair_count -= num_hash[l_num][1]
                num_hash[l_num][0] -= 1
                num_hash[l_num][1] = (
                    num_hash[l_num][0] * (num_hash[l_num][0] - 1)
                ) // 2
                pair_count += num_hash[l_num][1]
                l += 1
        #         print('num_hash: ', num_hash)
        #         print('pair_count: ', pair_count)
        #         print('.....')
        #     print('============================================')

        # print('good_subarr: ', good_subarr)
        return good_subarr

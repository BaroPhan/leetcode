"""
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum, remainder = divmod(sum(nums), 2)

        # If the sum of nums is odd, we cannot partition it into two equal subsets
        if remainder:
            return False

        # Initialize a boolean array that will keep track of possible sums
        can_partition = [True] + [False] * total_sum

        # Loop through each number in the nums array
        for num in nums:
            # Check each possible sum in reverse (to avoid using the same number twice)
            for j in range(total_sum, num - 1, -1):
                # Update the can_partition array
                # True if the number itself can form the sum
                # or if the sum can be formed by adding the number to a previously possible sum
                can_partition[j] = can_partition[j] or can_partition[j - num]

        # The last element in the can_partition array indicates if we can partition
        # nums into two equal subsets
        return can_partition[total_sum]

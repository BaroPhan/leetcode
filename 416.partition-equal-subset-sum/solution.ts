/*
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
*/

function canPartition(nums: number[]): boolean {
    const sumNums = nums.reduce((acc, elem) => acc + elem, 0)
    if (sumNums % 2 !== 0) return false
    const targetSum = sumNums / 2
    const canPartition = [true, ...Array(targetSum).fill(false)]

    for (let num of nums) {
        for (let j = targetSum; j >= num; --j) {
            canPartition[j] = canPartition[j] || canPartition[j - num]
        }
    }
    return canPartition[targetSum]
};
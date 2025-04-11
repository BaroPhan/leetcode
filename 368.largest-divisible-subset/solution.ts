/*
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
*/

function largestDivisibleSubset(nums: number[]): number[] {
    nums.sort((a, b) => a - b)
    const n = nums.length
    let k = 0
    const f = Array(n).fill(1)
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] % nums[j] === 0) {
                f[i] = Math.max(f[i], f[j] + 1)
            }
            if (f[k] < f[i])
                k = i
        }
    }
    let arrSize = f[k]
    let currPos = k
    const ans: number[] = []
    while (arrSize > 0) {
        if (nums[k] % nums[currPos] === 0 && f[currPos] === arrSize) {
            ans.push(nums[currPos])
            k = currPos
            arrSize -= 1
        }
        currPos -= 1
    }
    return ans
};

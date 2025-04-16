/*
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
*/

function countGood(nums: number[], k: number): number {
    const n = nums.length
    const hash = {}

    let pairCount = 0
    let goodSubarr = 0
    let l = 0

    if (n < 2) return goodSubarr

    for (let r = 0; r < n; r++) {
        const r_num = nums[r]
        if (!hash[r_num])
            hash[r_num] = { freq: 1, pair: 0 }
        else {
            pairCount -= hash[r_num].pair
            hash[r_num].freq += 1
            hash[r_num].pair = Math.floor((hash[r_num].freq * (hash[r_num].freq - 1)) / 2)
            pairCount += hash[r_num].pair
        }

        while (pairCount >= k && l <= r) {
            goodSubarr += (n - r)
            const l_num = nums[l]
            pairCount -= hash[l_num].pair
            hash[l_num].freq -= 1
            hash[l_num].pair = Math.floor((hash[l_num].freq * (hash[l_num].freq - 1)) / 2)
            pairCount += hash[l_num].pair
            l += 1
        }
    }
    return goodSubarr
};
/*
 * @lc app=leetcode id=1749 lang=typescript
 *
 * [1749] Maximum Absolute Sum of Any Subarray
 */

// @lc code=start
function maxAbsoluteSum(nums: number[]): number {
    let max = nums[0],
        min = nums[0],
        track_max = nums[0],
        track_min = nums[0];
    for (let i = 1; i < nums.length; i++) {
        track_max = Math.max(track_max + nums[i], nums[i])
        max = Math.max(track_max, max)
        track_min = Math.min(track_min + nums[i], nums[i])
        min = Math.min(track_min, min)
    }
    return Math.max(Math.abs(min), max)
};
// @lc code=end
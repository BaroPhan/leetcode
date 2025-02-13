/*
 * @lc app=leetcode id=3066 lang=typescript
 *
 * [3066] Minimum Operations to Exceed Threshold Value II
 */

// @lc code=start
function minOperations(nums: number[], k: number): number {
    nums.sort((a, b) => a - b)
    const b: number[] = []
    for (let i = 0, j = 0, count = 0, x, y; ; count += 1) {
        if (i < nums.length && (j >= b.length || nums[i] <= b[j])) {
            x = nums[i]; i += 1
        }
        else { x = b[j]; j += 1 }

        if (x >= k) { return count }

        if (i < nums.length && (j >= b.length || nums[i] <= b[j])) {
            y = nums[i]; i += 1
        }
        else { y = b[j]; j += 1 }
        b.push(x * 2 + y);
    }
};
// @lc code=end
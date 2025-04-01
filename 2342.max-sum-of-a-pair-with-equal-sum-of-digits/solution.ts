/*
 * @lc app=leetcode id=2342 lang=typescript
 *
 * [2342] Max Sum of a Pair With Equal Sum of Digits
 */

// @lc code=start
function maximumSum(nums: number[]): number {
    let max = -1
    const hashMap: Record<number, number> = {}
    for (const num of nums) {
        const sumValue = num.toString().split('').reduce((acc, val) => acc + parseInt(val), 0)
        if (!hashMap[sumValue])
            hashMap[sumValue] = num
        else {
            if (max < num + hashMap[sumValue]) max = num + hashMap[sumValue]
            hashMap[sumValue] = Math.max(num, hashMap[sumValue])
        }
    }
    return max
};
// @lc code=end
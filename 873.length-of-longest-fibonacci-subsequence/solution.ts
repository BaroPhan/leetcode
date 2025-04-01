/*
 * @lc app=leetcode id=873 lang=typescript
 *
 * [873] Length of Longest Fibonacci Subsequence
 */

// @lc code=start
function lenLongestFibSubseq(arr: number[]): number {
    const numSet = new Set(arr);
    let maxLen = 0;
    const n = arr.length;

    // Try all possible first two numbers of the sequence
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            // Start with the first two numbers
            let prev = arr[j];
            let curr = arr[i] + arr[j];
            let currLen = 2;

            // Keep finding the next Fibonacci-like number
            while (numSet.has(curr)) {
                const temp = curr;
                curr = curr + prev;
                prev = temp;
                currLen++;
                maxLen = Math.max(maxLen, currLen);
            }
        }
    }
    return maxLen;
};
// @lc code=end


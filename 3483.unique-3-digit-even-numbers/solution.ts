/*
 * @lc app=leetcode id=1910 lang=typescript
 *
 * 3483. Unique 3-Digit Even Numbers
 * https://leetcode.com/problems/unique-3-digit-even-numbers
 */

// @lc code=start
function totalNumbers(digits: number[]): number {
    const freq = new Array(10).fill(0);
    for (const d of digits) {
        freq[d]++;
    }
    let count = 0;
    for (let units = 0; units < 10; units += 2) {
        if (freq[units] === 0) continue;
        freq[units]--;
        for (let tens = 0; tens < 10; tens++) {
            if (freq[tens] === 0) continue;
            freq[tens]--;
            count += freq.slice(1, 10).filter(e => e > 0).length;
            freq[tens]++;
        }
        freq[units]++;
    }
    return count;
};
// @lc code=end

console.log(totalNumbers([1,2,3,4]));
console.log(totalNumbers([0,2,2]));
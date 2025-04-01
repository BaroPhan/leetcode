/*
 * @lc app=leetcode id=1780 lang=typescript
 *
 * [1780] Check if Number is a Sum of Powers of Three
 */

// @lc code=start
function checkPowersOfThree(n: number): boolean {
    if (n === 2) return false
    let boolean = false
    const sum: [number, number[]] = [n, []];
    while (sum[0] > 0) {
        for (let i = 0; i < n; i++) {
            if (3 ** i === sum[0] && !sum[1].includes(i)) {
                sum[0] -= 3 ** i
                sum[1].push(i)
                break
            }
            else if (3 ** i > sum[0] && !sum[1].includes(i - 1)) {
                sum[0] -= 3 ** (i - 1)
                sum[1].push(i - 1)
                break
            }
            else continue
        }
        if (sum[0] === 0) { boolean = true; break }
        else if (sum[0] < 0) { boolean = false; break }
    }
    return boolean
};
// @lc code=end
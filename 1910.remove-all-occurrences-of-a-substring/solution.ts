/*
 * @lc app=leetcode id=1910 lang=typescript
 *
 * [1910] Remove All Occurrences of a Substring
 */

// @lc code=start
function removeOccurrences(s: string, part: string): string {
    let res = s
    while (res.includes(part)) {
        const pos = res.indexOf(part);
        res = res.slice(0, pos) + res.slice(pos + part.length)
    }
    return res

};
// @lc code=end


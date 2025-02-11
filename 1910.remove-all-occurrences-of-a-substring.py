#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#


# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = s
        while part in res:
            pos = res.index(part)
            res = res[:pos] + res[pos + len(part) :]
        return res


# @lc code=end
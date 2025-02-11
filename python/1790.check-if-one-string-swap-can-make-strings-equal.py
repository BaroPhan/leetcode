#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2) and sum([i != j for i, j in zip(s1, s2)]) in [0,2]
        
# @lc code=end

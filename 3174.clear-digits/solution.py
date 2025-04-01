#
# @lc app=leetcode id=3174 lang=python3
#
# [3174] Clear Digits
#


# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        num_pos = []
        for index, value in enumerate(s):
            if value.isnumeric():
                num_pos.append(index)
        res = s
        for index, value in enumerate(num_pos):
            value = value - (2 * index)
            res = res[: value - 1] + res[value + 1 :]
        return res


# @lc code=end
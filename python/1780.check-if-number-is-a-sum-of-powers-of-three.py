#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#

# @lc code=start


import math


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 2:
            return False
        boolean = False
        sum = [n, []]
        while sum[0] > 0:
            for i in range(0, n):
                if 3**i == sum[0] and i not in sum[1]:
                    sum[0] -= 3**i
                    sum[1].append(i)
                    break
                elif 3**i > sum[0] and i - 1 not in sum[1]:
                    sum[0] -= 3 ** (i - 1)
                    sum[1].append(i - 1)
                    break
                else:
                    continue

            if sum[0] == 0:
                boolean = True
                break
            elif sum[0] < 0:
                break
        return boolean


# @lc code=end

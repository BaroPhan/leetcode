#
# @lc app=leetcode id=1910 lang=python3
#
# 3483. Unique 3-Digit Even Numbers
# https://leetcode.com/problems/unique-3-digit-even-numbers
#


# @lc code=start
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        count = 0
        for units in range(0, 10, 2):
            if not freq[units]:
                continue
            freq[units] -= 1
            for tens in range(10):
                if not freq[tens]:
                    continue
                freq[tens] -= 1
                count += sum(1 for h in range(1, 10) if freq[h])
                freq[tens] += 1
            freq[units] += 1
        return count
            

if __name__ == "__main__":
    print(Solution().totalNumbers([1,2,3,4]))
    print(Solution().totalNumbers([0,2,2]))

# @lc code=end
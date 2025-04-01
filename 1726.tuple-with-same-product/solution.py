#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#

# @lc code=start
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = 0
        product_map = {}
        for index, value in enumerate(nums):
            for j in range(index + 1, len(nums)):
                product = value * nums[j]
                if product not in product_map:
                    product_map[product] = 1
                else:
                    product_map[product] += 1
        return sum(2 * ((i - 1) * 2) * i for i in product_map.values() if i > 1)


# @lc code=end

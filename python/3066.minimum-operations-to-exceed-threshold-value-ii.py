#
# @lc app=leetcode id=3066 lang=python3
#
# [3066] Minimum Operations to Exceed Threshold Value II
#


# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        b = []
        i = j = count = 0
        
        while True:
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                x = a[i]
                i += 1
            else:
                x = b[j]
                j += 1
            
            if x >= k:
                return count
            
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                y = a[i]
                i += 1
            else:
                y = b[j]
                j += 1
            
            b.append(2 * x + y)
            count += 1
        return -1


# @lc code=end
nums = [2, 11, 10, 1, 3]
k = 10

small_val_list = sorted(nums)
count = 0
a = sorted(nums)
b = []
i = j = count = 0

print(a)
while True:
    print("begin", i, j, b)
    if i < len(a) and (j >= len(b) or a[i] <= b[j]):
        x = a[i]
        i += 1
    else:
        x = b[j]
        j += 1

    if x >= k:
        print("count: ", count)
        break

    if i < len(a) and (j >= len(b) or a[i] <= b[j]):
        y = a[i]
        i += 1
    else:
        y = b[j]
        j += 1
    print("x + y", x, y)
    b.append(2 * x + y)
    count += 1
    print("count: ", count)

"""
1399. Count Largest Group
https://leetcode.com/problems/count-largest-group
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.



Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.


Constraints:
1 <= n <= 104
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash = {}
        max = 0
        count = 0
        for i in range(1,n+1):
            digit_sum = sum([int(char) for char in str(i)])
            hash[digit_sum] = hash.get(digit_sum, 0) + 1
        for val in hash.values():
            if val > max:
                max = val
                count = 1
            elif val == max:
                count += 1
        return count
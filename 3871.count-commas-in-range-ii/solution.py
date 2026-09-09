'''
3871. Count Commas in Range II
https://leetcode.com/problems/count-commas-in-range-ii/
You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
 

Example 1:

Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:

Input: n = 998

Output: 0

Explanation:

​​​​​​​All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

Constraints:
1 <= n <= 1015
'''

class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        threshold = 1000          # first place a comma appears
        while threshold <= n:
            numbers_with_this_comma = n - threshold + 1
            total += numbers_with_this_comma
            threshold = threshold * 1000   # next comma level: 1e6, 1e9, ...
        return total

if __name__ == "__main__":
    print(Solution().countCommas(1004590)) # expected 1008182
    print(Solution().countCommas(154729)) # expected 153730
    print(Solution().countCommas(1026669)) # expected 1052340
    print(Solution().countCommas(1173494)) # expected 1345990
    print(Solution().countCommas(2074499)) # expected 3148000
    print(2//3, 2%3)
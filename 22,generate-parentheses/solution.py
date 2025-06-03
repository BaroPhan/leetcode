'''
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
'''


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_used: int, close_used: int, current: str) -> None:
            if open_used + close_used == 2 * n:
                result.append(current)
                return
            if open_used < n:
                backtrack(open_used + 1, close_used, current + '(')
            if close_used < open_used:
                backtrack(open_used, close_used + 1, current + ')')

        result = []
        backtrack(0, 0, "")
        return result

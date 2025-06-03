/*
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
*/

function generateParenthesis(n: number): string[] {
  const result: string[] = [];

  function recursive(open = 0, close = 0, current = "") {
    if (open + close === 2 * n) result.push(current);
    if (open < n) recursive(open + 1, close, current + "(");
    if (close < open) recursive(open, close + 1, current + ")");
  }

  recursive(0, 0);
  return result;
}

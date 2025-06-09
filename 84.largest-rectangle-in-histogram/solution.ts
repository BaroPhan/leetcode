/*
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
*/

function largestRectangleArea(heights: number[]): number {
  heights.push(0);
  const stack = [0];
  let maxA = 0;
  for (let i = 1; i < heights.length; i++) {
    const curr = heights[i];
    // console.log('curr: ', curr, i)
    let currA = 0;
    while (stack.length > 0 && heights[stack[stack.length - 1]] > curr) {
      const idx = stack.pop()!;
      const width = i - (stack.length > 0 ? stack[stack.length - 1] : -1) - 1;
      const area = heights[idx] * width;
      // console.log('area: ', area)
      currA = Math.max(currA, area);
    }
    stack.push(i);
    maxA = Math.max(currA, maxA);
  }
  return maxA;
}

'''
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
'''


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
        for idx, h in enumerate(heights):
            # print('idx: ', idx, h)
            if not stack:
                stack.append(idx)
            else:
                curr_area = 0
                # print('stack: ', stack, stack[-1],  heights[stack[-1]])
                while stack and heights[stack[-1]] > h:
                    i = stack.pop()
                    # print('cur i: ', i)
                    width = idx - (stack[-1] if stack else -1) - 1
                    # print('width: ', width)
                    area = heights[i] * width
                    # print('area: ', area)
                    curr_area = max(curr_area, area)

                stack.append(idx)
                # print('curr_area: ', curr_area)
                max_area = max(curr_area, max_area)
            # print('stack: ', stack)
            # print('======================')
        # print('max_area: ', max_area)
        return max_area

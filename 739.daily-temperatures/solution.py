"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        count = 0
        for idx, temp in enumerate(temperatures):
            # print('temp: ', temp)
            # print('idx: ', idx)
            while stack and count <= 50:
                s_temp, s_idx = stack[-1]
                # print('s_temp: ', s_temp)
                # print('s_idx: ', s_idx)
                if temp > s_temp:
                    result[s_idx] = idx - s_idx
                    stack.pop()
                else:
                    break
                # print('result: ', result)
                # print('stack: ', stack)
                # print('=====================')
            stack.append((temp, idx))
        #     print('stack: ', stack)
        #     print('_____________')
        # print('result: ', result)
        return result

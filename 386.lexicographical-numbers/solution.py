'''
386. Lexicographical Numbers
https://leetcode.com/problems/lexicographical-numbers
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:
1 <= n <= 5 * 104
'''


from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def recursion(curr):
            # print("curr: ", curr)
            result.append(curr)
            for d in range(10):
                child = curr * 10 + d
                # print('child: ', child)
                if child > n:
                    return
                recursion(child)

        for i in range(1, 10):
            if i > n:
                break
            recursion(i)
            # print("====================")
        # print('result: ', result)
        return result

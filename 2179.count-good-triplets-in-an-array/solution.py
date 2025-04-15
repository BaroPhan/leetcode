"""
2179. Count Good Triplets in an Array
https://leetcode.com/problems/count-good-triplets-in-an-array
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.



Example 1:

Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
Output: 1
Explanation:
There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3).
Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
Example 2:

Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
Output: 4
Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).


Constraints:
n == nums1.length == nums2.length
3 <= n <= 105
0 <= nums1[i], nums2[i] <= n - 1
nums1 and nums2 are permutations of [0, 1, ..., n - 1].
"""

from typing import List


class BinaryIndexedTree:
    def __init__(self, size):
        self.size = size + 2  # Extra space to handle edge cases
        self.tree = [0] * self.size

    def update(self, index, value):
        index += 1  # Shift index to match 1-based indexing
        while index < self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        index += 1  # Shift index to match 1-based indexing
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos_in_nums2 = [0] * n
        for idx, val in enumerate(nums2):
            pos_in_nums2[val] = idx

        transformed = [pos_in_nums2[val] for val in nums1]

        left_tree = BinaryIndexedTree(n)
        right_tree = BinaryIndexedTree(n)

        # Initialize right_tree with counts of all elements
        for val in transformed:
            right_tree.update(val, 1)

        total_good_triplets = 0
        for val in transformed:
            right_tree.update(val, -1)  # Remove current element from right_tree
            left_count = left_tree.query(val - 1)
            right_count = right_tree.query(n - 1) - right_tree.query(val)
            total_good_triplets += left_count * right_count
            left_tree.update(val, 1)  # Add current element to left_tree

        return total_good_triplets

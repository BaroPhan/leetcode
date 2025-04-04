"""
1123. Lowest Common Ancestor of Deepest Leaves
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.


Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of itself.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.


Constraints:
The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 1000
The values of the nodes in the tree are unique.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDeepestLeaves(self, root: Optional[TreeNode], layer=1, hash_node={}):
        if not root:
            return hash_node
        if not root.left and not root.right:
            if layer in hash_node:
                hash_node[layer].append(root)
            else:
                hash_node[layer] = [root]
            return hash_node[max(list(hash_node.keys()))]
        layer += 1
        self.findDeepestLeaves(
            root.left,
            layer,
            hash_node,
        )
        self.findDeepestLeaves(
            root.right,
            layer,
            hash_node,
        )
        return hash_node[max(list(hash_node.keys()))]

    def findLca(
        self,
        root: Optional[TreeNode],
        leaves: list[TreeNode],
    ):
        # print("root: ", root)
        # print("leaves before: ", leaves)

        if not root:
            return leaves
        self.findLca(root.left, leaves)
        self.findLca(root.right, leaves)
        # print('root after: ', root)
        if len(leaves) == 1:
            return leaves
        if any(child in leaves for child in (root.left, root.right)):
            if root.left in leaves:
                leaves.remove(root.left)
            if root.right in leaves:
                leaves.remove(root.right)
            if root not in leaves:
                leaves.append(root)
            # print("leaves after: ", leaves)
            # print("=======================================")
            return leaves

        return leaves

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        layer = 1
        deepest_leaves_hash = self.findDeepestLeaves(root)
        # print("hash_node: ", deepest_leaves_hash, len(deepest_leaves_hash))
        if len(deepest_leaves_hash) == 1:
            return deepest_leaves_hash[0]
        else:
            leaves = self.findLca(root, list(deepest_leaves_hash))
            # print("final leaves: ", leaves)
            return leaves[0]

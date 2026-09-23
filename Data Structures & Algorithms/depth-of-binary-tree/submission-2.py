# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        arr = [[root, 1]]
        res = 0

        while arr:
            node, depth = arr.pop()

            if node:
                res = max(res, depth)
                arr.append([node.left, depth + 1])
                arr.append([node.right, depth + 1])

        return res
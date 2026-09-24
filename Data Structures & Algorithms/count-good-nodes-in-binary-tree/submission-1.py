# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, ma):
            if not node:
                return 0
            # res = 0
            if node.val >= ma:
                res = 1
                ma = node.val
            else:
                res = 0

            res += dfs(node.left, ma)
            res += dfs(node.right, ma)

            return res

        return dfs(root, root.val)
        
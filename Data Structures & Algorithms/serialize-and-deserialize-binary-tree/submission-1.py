# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ','.join(res)

        # def dfs(node):
        #     if not node:
        #         res.append('N')
        #         return
        #     res.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(',')
        if values[0] == 'N':
            return None
        
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()
            if values[i] != 'N':
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1
            if values[i] != 'N':
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        return root

        # def dfs():
        #     if values[self.i] == 'N':
        #         self.i += 1
        #         return None
        #     node = TreeNode(int(values[self.i]))
        #     self.i += 1
        #     node.left = dfs()
        #     node.right = dfs()
        #     return node

        # return dfs()

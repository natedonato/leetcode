# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.k = k
        return self.dfs(root)

    
    # [count, kth]
    def dfs(self, node):
        if not node:
            return None
        
        left = self.dfs(node.left)

        if left is not None:
            return left
        self.count += 1
        
        if self.count == self.k:
            return node.val
        
        return self.dfs(node.right)

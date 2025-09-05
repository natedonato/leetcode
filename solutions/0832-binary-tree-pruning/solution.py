# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)

    def dfs(self, node):
        if node.left:
            node.left = self.dfs(node.left)
        if node.right:
            node.right = self.dfs(node.right)
        
        if not node.left and not node.right and node.val != 1:
            return None
        else:
            return node

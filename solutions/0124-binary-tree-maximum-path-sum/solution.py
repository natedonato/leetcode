# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf
        self.dfs(root)

        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        sub_sum = max(left + node.val, right + node.val, node.val)

        self.max_sum = max(sub_sum, self.max_sum, left + right + node.val)
        return sub_sum


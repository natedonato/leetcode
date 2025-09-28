# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
        
    def dfs(self,node):
        if not node:
            return [True, 0]
        height = 1

        [leftBalanced, leftHeight] = self.dfs(node.left)
        [rightBalanced, rightHeight] = self.dfs(node.right)

        if not leftBalanced or not rightBalanced or abs(leftHeight - rightHeight) > 1:
            return [False, 0]

        return [True, max(leftHeight, rightHeight) + 1]

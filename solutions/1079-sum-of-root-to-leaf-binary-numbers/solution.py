# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node, num):
            num = (num << 1) + node.val

            if not node.left and not node.right:
                self.total += num
                return
            if node.left:
                dfs(node.left, num)
            if node.right:
                dfs(node.right, num)

        dfs(root, 0)

        return self.total

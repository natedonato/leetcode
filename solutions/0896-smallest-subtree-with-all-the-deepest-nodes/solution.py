# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root, 0)[0]

    def dfs(self, node, depth):
        if not node:
            return [None, depth]

        depth += 1

        left = self.dfs(node.left, depth +1 )
        right = self.dfs(node.right, depth +1)

        if left[1] == right[1]:
            return [node, left[1]]
        elif left[1] > right[1]:
            return left
        else:
            return right

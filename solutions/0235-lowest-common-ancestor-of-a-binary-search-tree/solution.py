# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q

        return self.dfs(root)[0]


    def dfs(self, node):
        count = 0

        if not node:
            return [None,0]

        if node == self.p or node == self.q:
            count += 1
        
        left = self.dfs(node.left)
        if left[1] >= 2:
            return left

        count += left[1]
        
        right = self.dfs(node.right)

        if right[1] >= 2:
            return right

        count += right[1]

        return [node, count]

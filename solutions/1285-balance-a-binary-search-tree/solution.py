# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.values = []
        self.dfs(root)

        return self.buildTree(0, len(self.values) - 1)

    def dfs(self, node):
        if node.left:
            self.dfs(node.left)

        self.values.append(node.val)

        if node.right:
            self.dfs(node.right)

    def buildTree(self, i, j):
        mid = (j-i) // 2 + i
        
        node = TreeNode(self.values[mid])

        if i < mid:
            node.left = self.buildTree(i, mid-1)
        
        if j > mid:
            node.right = self.buildTree(mid+1, j)

        return node

        

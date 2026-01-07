# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max_product = 0
        self.mod = 1_000_000_007
        self.total_sum = None
        self.total_sum = self.treesum(root)
        self.treesum(root)
        return self.max_product % self.mod


    def treesum(self, node):
        if not node:
            return 0
        
        l = self.treesum(node.left)
        r = self.treesum(node.right)
        if self.total_sum:
            self.max_product = max(self.max_product, (self.total_sum - l)* l, (self.total_sum - r) * r) 

        return node.val + l + r

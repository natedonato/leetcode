# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        return self.solve(0,0, len(preorder))
    def solve(self, pstart, istart, size):
        if size <= 0:
            return None

        root = TreeNode(self.preorder[pstart])
        if size == 1:
            return root

        left_subproblem_size = 0
        while(self.preorder[pstart] != self.inorder[istart + left_subproblem_size]):
            left_subproblem_size += 1
        
        left_sub = self.solve(pstart + 1, istart, left_subproblem_size)

        right_sub = self.solve(pstart + left_subproblem_size + 1, istart + left_subproblem_size + 1, size - left_subproblem_size - 1)

        root.left = left_sub
        root.right = right_sub

        return root

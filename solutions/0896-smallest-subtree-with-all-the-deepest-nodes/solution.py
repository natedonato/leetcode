# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.getDeepSub(root, 1)[1]

    # return [deepest_depth, deepest_node_containing]
    def getDeepSub(self, node, current_depth):
        if not node:
            return [-1, None]

        left = self.getDeepSub(node.left, current_depth + 1)
        right = self.getDeepSub(node.right, current_depth + 1)

        if left[0] == right[0]:
            if left[0] == -1:
                return[current_depth, node]
            return [left[0], node]
        return max(left, right)
        

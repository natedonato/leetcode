# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # [ancestor, depth]
        def dfs(root):
            # base
            if not root:
                return (root, 0)
            
            left_node, left_depth = dfs(root.left)
            right_node, right_depth = dfs(root.right)

            if left_depth == right_depth:
                return (root, left_depth + 1)
            elif left_depth > right_depth:
                return (left_node, left_depth + 1)
            else:
                return(right_node, right_depth + 1)

        return dfs(root)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]


    def dfs(self, node: TreeNode) -> [bool, int, int]:
        max_val = node.val
        min_val = node.val

        if node.left:
            [left_valid, left_min, left_max] = self.dfs(node.left)
            
            if left_valid == False or left_max >= node.val:
                return [False, 0, 0]
            else:
                min_val = min(max_val, left_min)

        if node.right: 
            [right_valid, right_min, right_max] = self.dfs(node.right)
            if right_valid == False or right_min <= node.val:
                return [False, 0, 0]
            else:
                max_val = max(right_max, max_val)

        return [True, min_val, max_val]

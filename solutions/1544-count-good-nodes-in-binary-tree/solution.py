# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        self.dfs(root)
        
        return self.count


        

    def dfs(self, node: TreeNode, prev_max: int = -math.inf) -> None:
        if node.val >= prev_max:
            self.count += 1

        prev_max = max(prev_max, node.val)
        if node.left:
            self.dfs(node.left, prev_max)
        if node.right:
            self.dfs(node.right, prev_max)
        

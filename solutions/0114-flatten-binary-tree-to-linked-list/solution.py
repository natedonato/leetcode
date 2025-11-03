# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # pre-order traversal: current -> left -> right
        
        #empty tree
        if not root:
            return None

        # no children, return root
        if not root.left and not root.right:
            return root

        # One child, make sure it is on the right
        if root.left and not root.right:            
            root.right = self.flatten(root.left)
            root.left = None
            return root
        if root.right and not root.left:
            root.right = self.flatten(root.right)
            return root

    # Two children:
        right_pointer = root.right
        left_solution = self.flatten(root.left)

        tail = left_solution
        while tail and tail.right:
            tail = tail.right

        tail.right = self.flatten(root.right)
        root.right = left_solution
        root.left = None

        return root

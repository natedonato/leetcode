# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.sub = None
        self.sub = self.serialize(subRoot)[1]

        return self.serialize(root)[0]
    

    def serialize(self, treenode):
        if not treenode:
            return [False, "X"]
        
        root = str(treenode.val)

        left = self.serialize(treenode.left)
        right = self.serialize(treenode.right)

        if left[0] or right[0]:
            return [True, ""]
        
        serial = root + "," + left[1] + "," + right[1]

        if self.sub is not None and serial == self.sub:
            return [True, serial]


        return [False, serial]

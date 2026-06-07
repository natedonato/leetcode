# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m = {}
        c = set()
        for edge in descriptions:
            parent, child, isLeft = edge
            c.add(child)
            if parent not in m:
                m[parent] = TreeNode(parent)
            
            if child not in m:
                m[child] = TreeNode(child)
            
            if isLeft == 1:
                m[parent].left = m[child]
            else:
                m[parent].right = m[child]

        for node in m:
            if node not in c:
                return m[node]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.buildTree(0, len(nums) - 1)

    def buildTree(self, i, j):
        mid = (j-i) // 2 + i
        
        node = TreeNode(self.nums[mid])

        if i < mid:
            node.left = self.buildTree(i, mid-1)
        
        if j > mid:
            node.right = self.buildTree(mid+1, j)

        return node

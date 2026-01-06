# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        out = 0
        level = 0

        q = deque([root])

        while q:
            level += 1
            current_sum = 0
            current_size = len(q)

            for i in range(current_size):
                node = q.popleft()
                current_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if current_sum > max_sum:
                out = level
                max_sum = current_sum

        return out


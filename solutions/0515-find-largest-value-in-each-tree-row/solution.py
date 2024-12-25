# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        output = []
        
        while queue:
            max = None
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                if node is None:
                    continue
                
                if max is None or node.val > max:
                    max = node.val
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            if max is not None:
                output.append(max)
        
        return output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = 0
        queue = deque([root])
        
        while queue:
            level = []
            depth += 1
            count = len(queue)
            
            for _ in range(count):
                node = queue.popleft()
                level.append(node)
                
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if depth % 2 == 0:
                for i in range(count // 2):
                    temp = level[i].val
                    level[i].val = level[-i - 1].val
                    level[-i - 1].val = temp
        
        return root
                
            

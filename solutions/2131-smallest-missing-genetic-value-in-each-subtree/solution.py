class TreeNode:
    def __init__(self, val, idx):
        self.val = val
        self.id = idx
        self.children = []
        self.parent = -1 
        self.smallest_missing = 1
    
    def __repr__(self):
        return str({"id": self.id, "val": self.val, "children": self.children, "parent": self.parent})

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        self.nodes = {}
        self.seen_vals = [0] * (len(nums) + 2)
        current_smallest_missing_value = 1

        n = len(parents)
        current_node = None
        for i in range(n):
            self.nodes[i] = TreeNode(nums[i], i)
            if nums[i] == 1:
                current_node = self.nodes[i]

        for i in range(n):
            self.nodes[i].parent = parents[i]
            if parents[i] > -1:
                self.nodes[parents[i]].children.append(self.nodes[i])

        while current_node:
            self.dfs(current_node)
            
            while self.seen_vals[current_smallest_missing_value] == 1:
                current_smallest_missing_value += 1
            
            current_node.smallest_missing = current_smallest_missing_value
            
            if current_node.parent == -1:
                break
            else:
                current_node = self.nodes[current_node.parent]

        out = []
        for i in range(n):
            out.append(self.nodes[i].smallest_missing)
        
        return out
    
    def dfs(self, node):
        if node.val < len(self.seen_vals) and not self.seen_vals[node.val] == 1:
            self.seen_vals[node.val] = 1
            for child in node.children:
                self.dfs(child)


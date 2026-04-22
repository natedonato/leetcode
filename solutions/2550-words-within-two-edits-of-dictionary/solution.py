class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = {}

        for word in dictionary:
            current_node = trie
            for char in word:
                if char not in current_node:
                    current_node[char] = {}
                current_node = current_node[char]

        out = []
        
        for word in queries:
            solved = False
            queue = deque([[trie, 0]])

            for char in word:
                l = len(queue)
                for i in range(l):
                    vals = queue.popleft()
                    node, skipped = vals                    
                    
                    if char in node:
                        queue.append([node[char], skipped])
                    
                    if skipped < 2:
                        for next_node in node.values():
                            queue.append([next_node, skipped + 1])
            
            if len(queue) > 0:
                out.append(word)

        return out

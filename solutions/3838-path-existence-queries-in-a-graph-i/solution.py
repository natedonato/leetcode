class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parents = []
        for i in range(n):
            parents.append(i)
        
        def find(node):
            if parents[node] == node:
                return node
            else:
                ans = find(parents[node])
                parents[node] = ans
                return ans
        
        def merge(n1,n2):
            if parents[n1] != parents[n2]:
                parents[n2] = parents[n1]
        

        for i in range(len(nums) - 1):
            v1 = nums[i]
            v2 = nums[i+1]
            if v2 - v1 <= maxDiff:
                merge(i,i+1)

        out = []
        
        for q in queries:
            n1, n2 = q
            if find(n1) == find(n2):
                out.append(True)
            else:
                out.append(False)

        return out

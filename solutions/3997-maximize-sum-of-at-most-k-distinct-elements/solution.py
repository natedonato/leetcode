class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        seen = set()
        h = []
        
        for n in nums:
            if n not in seen:
                if len(h) < k:
                    heapq.heappush(h,n)
                else:
                    heapq.heappushpop(h,n)

                seen.add(n)
        

        out = []
        while h:
            out.append(heapq.heappop(h))
        out.reverse()

        return out

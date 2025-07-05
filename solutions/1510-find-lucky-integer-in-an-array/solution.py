class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        lucky = -1

        for key, val in counts.items():
            if(val == key):
                lucky = max(lucky, key)
            
        
        return lucky

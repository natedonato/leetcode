class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        s = Counter()
        for d in dominoes:
            if(d[0] > d[1]):
                t = d[1]
                d[1] = d[0]
                d[0] = t
            

            s[(d[0],d[1])] += 1
        count = 0
        for n in s.values():
            count += (n - 1)*n // 2
        
        return count

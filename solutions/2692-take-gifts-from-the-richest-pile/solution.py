class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort();
        
        for i in range(0,k):
            gifts[-1] = math.floor(math.sqrt(gifts[-1]));
            gifts.sort();
        
        sum = 0;
        
        for gift in gifts:
            sum += gift
            
        return sum

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        minimum_el = min(min(basket1),min(basket2))
        counts1 = collections.Counter(basket1)
        counts2 = collections.Counter(basket2)

        items_1 = []
        items_2 = []

        for key in counts1:
            key_count_1 = counts1[key]
            key_count_2 = counts2[key]

            if (key_count_1 + key_count_2) % 2 != 0:
                return -1
            
            if(key_count_1 > key_count_2):
                total = (key_count_1 - key_count_2) // 2
                items_1.extend([key] * total)

        for key in counts2:
            key_count_1 = counts1[key]
            key_count_2 = counts2[key]

            if (key_count_1 + key_count_2) % 2 != 0:
                return -1
            
            if(key_count_2 > key_count_1):
                total = (key_count_2 - key_count_1) // 2
                items_2.extend([-key] * total)

        score = 0

        heapq.heapify(items_1)
        heapq.heapify(items_2)

        while(items_1):
            item_1 = heapq.heappop(items_1)
            item_2 = -heapq.heappop(items_2)
            score += min(item_1, item_2, 2*minimum_el)
        
        return score


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        l = len(baskets)
        r = int(math.sqrt(l))

        num_buckets = math.ceil(l / r)

        buckets = [0] * num_buckets

        for i in range(num_buckets):
            start_idx = i * r
            buckets[i] = max(baskets[start_idx:start_idx + r] )

        unplaced = 0
        
        for fruit in fruits:
            score = 1
            for i in range(len(buckets)):
                if fruit <= buckets[i]:
                    score = 0
                    start_idx = i * r
                    j = 0
                    while baskets[start_idx + j] < fruit:
                        j += 1
                    baskets[start_idx + j] = 0
                    buckets[i] = max(baskets[start_idx:start_idx + r])
                    break

            unplaced += score

        return unplaced


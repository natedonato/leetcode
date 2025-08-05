class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for fruit in fruits:
            placed = False
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = 0
                    placed = True
                    break
            if placed == False:
                unplaced += 1

        return unplaced

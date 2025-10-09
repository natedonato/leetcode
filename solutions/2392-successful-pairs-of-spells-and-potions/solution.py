class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        self.potions = potions
        self.potions.sort()
        self.target = success

        out = []

        for spell in spells:
            out.append(self.bsearch(spell))

        return out

    def bsearch(self, spell):
        if self.potions[-1] * spell < self.target:
            return 0
        
        l = 0
        r = len(self.potions)

        while l < r:
            mid = l + ((r-l) // 2)

            if self.potions[mid] * spell >= self.target:
                r = mid
            else:
                l = mid + 1

        return len(self.potions) - l

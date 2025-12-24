class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse = True)
        
        i = 0
        while total > 0:
            total -= capacity[i]
            i += 1

        return i

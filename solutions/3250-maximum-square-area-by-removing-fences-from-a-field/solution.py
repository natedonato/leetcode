class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        max_size = -1
        hSizes = set()
        hFences.extend([1, m])
        vFences.extend([1, n])

        for i in range(len(hFences) - 1):
            for j in range(i+1, len(hFences)):
                diff = abs(hFences[i] - hFences[j])
                hSizes.add(diff)

        for i in range(len(vFences) - 1):
            for j in range(i+1, len(vFences)):    
                diff = abs(vFences[i] - vFences[j])
                if diff in hSizes:
                    max_size = max(max_size, diff)

        return -1 if max_size == -1 else max_size ** 2 % (10**9 + 7)


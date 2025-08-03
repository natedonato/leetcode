class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left_idx = 0
        max_fruits = 0

        while  left_idx < len(fruits) and fruits[left_idx][0] + k < startPos:
            left_idx += 1

        right_idx = left_idx
        current_total = 0

        while(left_idx < len(fruits) and fruits[left_idx][0] <= startPos + k):
 
            leftPos = fruits[left_idx][0]
            if leftPos >= startPos:
                rightBound = startPos + k
            else:
                rightBound = max(leftPos + k - (startPos - leftPos), (k - (startPos - leftPos)) // 2 + startPos)

            while(right_idx < len(fruits) and fruits[right_idx][0] <= rightBound):
                current_total += fruits[right_idx][1]
                right_idx += 1

            max_fruits = max(max_fruits, current_total)

            current_total -= fruits[left_idx][1]
            left_idx += 1
        
        return max_fruits

        

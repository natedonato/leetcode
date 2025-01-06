class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        sum = 0
        num_right = 0
        for i, box in enumerate(boxes):
            if box == '1':
                sum += i
                num_right += 1
        
        
        
        output = [sum]


            
        num_left = 0

        
        for i in range(1,len(boxes)):
            num_right -= int(boxes[i - 1])
            num_left += int(boxes[i - 1])
            
            sum -= num_right
            sum += num_left
            output.append(sum)
            
        return output

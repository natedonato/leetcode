class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        self.count = Counter(nums[:k])
        self.x = x
        output = [self.xSumSub(self.count)]

        for i in range(k, len(nums)):
            self.count[nums[i-k]] = self.count[nums[i-k]] - 1
            self.count[nums[i]] = self.count[nums[i]] + 1
            output.append(self.xSumSub(self.count))
        
        return output
        

    def xSumSub(self, count):
        # min-heap (frequency, element)
        
        h = []
        for c in count:
            if len(h) < self.x:
                heapq.heappush(h, (count[c], c))
            else:
                heapq.heappushpop(h, (count[c],c))

        sub_sum = 0
        for item in h:
            sub_sum += item[0] * item[1]

        return sub_sum

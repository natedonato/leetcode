class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        largest = -1
        counts = Counter(nums)

        if(k == len(nums)):
            for item in counts.items():
                largest = max(largest, item[0])
            return largest
        elif(k == 1):
            for item in counts.items():
                if(item[1] == 1):
                    largest = max(largest, item[0])
            return largest  
        else:
            first = counts[nums[0]]
            last = counts[nums[-1]]
            if first == 1:
                largest = max(largest, nums[0])
            if last == 1:
                largest = max(largest, nums[-1])
            return largest


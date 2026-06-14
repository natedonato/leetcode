class Solution:
    def getLength(self, nums: List[int]) -> int:
        maxLength = 0
        
        for i in range(len(nums)):
            c = Counter()
            current_max = 0
            for j in range(i, len(nums)):
                val = nums[j]
                c.update([val])
                current_max = max(current_max, c[val])
                if len(c) == 1:
                    maxLength = max(maxLength, j - i + 1)
                
                elif current_max % 2 == 0:
                    valid = True
                    s = set(c.values())
                    if len(s) != 2:
                        valid = False

                    if valid:
                        a = list(s)
                        a.sort()
                        if a[0] * 2 != a[1]:
                            valid = False
                    
                    if valid:
                        maxLength = max(maxLength, j - i + 1)

        return maxLength

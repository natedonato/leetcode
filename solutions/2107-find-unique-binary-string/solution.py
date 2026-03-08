class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set()
        for num in nums:
            s.add(int(num,2))

        for i in range(2 ** len(nums)):
            print(i)
            if i not in s:
                out = bin(i)[2:]
                out = "0" * (len(nums) - len(out)) + out
                return out

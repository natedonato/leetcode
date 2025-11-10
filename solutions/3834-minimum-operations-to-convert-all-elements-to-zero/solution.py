class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = [0]
        ops = 0

        for n in nums:
            while stack[-1] > n:
                stack.pop()

            if n != stack[-1]:
                ops += 1
                stack.append(n)

        return ops

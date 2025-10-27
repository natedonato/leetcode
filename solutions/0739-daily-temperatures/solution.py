class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]

            while stack and t > stack[-1][0]:
                prev_index = stack[-1][1]
                out[prev_index] = i - prev_index
                stack.pop()

            stack.append([t,i])

        return out 
    

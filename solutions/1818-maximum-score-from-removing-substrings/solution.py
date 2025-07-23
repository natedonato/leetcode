class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            first = "ab"
            second = "ba"
        else:
            first = "ba"
            second = "ab"

        score = 0

        stack = []
        for c in s:
            if stack and stack[-1] == first[0] and c == first[1]:
                score += max(x,y)
                stack.pop()
            else:
                stack.append(c)

        s = stack
        stack = []

        for c in s:
            if stack and stack[-1] == second[0] and c == second[1]:
                score += min(x,y)
                stack.pop()
            else:
                stack.append(c)

        return score

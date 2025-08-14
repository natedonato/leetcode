class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [("x",-1)]


        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append((char, i))
            if char == ")":
                if len(stack) > 0 and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((char,i))

        stack.append(("x", len(s)))

        best = 0
        for i in range(1, len(stack)):
            prev_idx = stack[i-1][1]
            current_idx = stack[i][1]

            best = max(best, current_idx - prev_idx - 1)

        return best 



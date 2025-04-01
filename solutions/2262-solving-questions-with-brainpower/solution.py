class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        l = len(questions)
        dp = [-1] * l

        def solve(i,l):
            if(i >= l):
                return 0
            if dp[i] != -1:
                return dp[i]
            current_question = questions[i]
            current_points = current_question[0]
            current_brainpower = current_question[1]
            take_score = current_points + solve(i + 1 + current_brainpower,l)
            skip_score = solve(i + 1,l)
            dp[i] =  max(take_score, skip_score)
            return dp[i] 

        return solve(0,l)

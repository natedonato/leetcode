class Solution:
    def countWinningSequences(self, s: str) -> int:
        
        def score(p1, p2):
            if p1 == p2:
                return 0
            elif (p1 == "F" and p2 == "E") or (p1 == "W" and p2 == "F") or (p1 == "E" and p2 == "W"):
                return 1
            else:
                return -1
        @cache
        def dp(idx, prev_thrown, score_diff):
            if idx == len(s):
                if score_diff > 0:
                    return 1
                else:
                    return 0

            rounds_remaining = len(s) - idx
            if rounds_remaining + score_diff <= 0:
                return 0

            if score_diff - rounds_remaining > 0:
                return (2 **rounds_remaining) % (1_000_000_000 + 7)


            alice = s[idx]

            count = 0
            for bob in "EFW":
                if bob == prev_thrown:
                    continue
                
                count += dp(idx + 1, bob, score_diff + score(bob, alice))

            return count % (1_000_000_000 + 7)

        return dp(0, None, 0)



class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0 for _ in range(n)]
        me = -math.inf

        for i in reversed(range(n)):
            ce = energy[i]
            if i + k < n:
                ce += dp[i+k]

            dp[i] = ce
            me = max(me, ce)

        return me

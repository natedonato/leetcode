class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        rounds = 0

        for task, count in c.items():
            if count < 2:
                return -1
            
            rounds += math.ceil(count/3)

        return rounds

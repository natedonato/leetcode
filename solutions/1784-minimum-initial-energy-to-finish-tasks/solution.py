class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda e: e[1] - e[0], reverse = True)
        
        l = 0
        r = 10000 * len(tasks)

        while l < r:
            mid = (r - l) // 2 + l

            if self.canDo(tasks, mid):
                r = mid
            else:
                l = mid + 1

        return l



    def canDo(self, tasks, energy):
        for task in tasks:
            if task[1] > energy:
                return False
            energy -= task[0]
            if energy < 0: 
                return False
        return True

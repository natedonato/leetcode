class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        s = set()
        for o in obstacles:
            s.add(tuple(o))
        pos = [0,0]

        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        current_dir = 0

        max_dist = 0

        for c in commands:
            if c == -2:
                current_dir -= 1
                current_dir %= 4
            elif c == -1:
                current_dir += 1
                current_dir %= 4
            else:
                for i in range(c):
                    pos[0] += dirs[current_dir][0]
                    pos[1] += dirs[current_dir][1]
                    if tuple(pos) in s:
                        pos[0] -= dirs[current_dir][0]
                        pos[1] -= dirs[current_dir][1]
                    max_dist = max(max_dist, pos[0] ** 2 + pos[1] ** 2)

        return max_dist

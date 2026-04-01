class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        bots = []

        for i in range(len(positions)):
            bots.append([positions[i], healths[i], directions[i],i])

        bots.sort()
        stack = []


        for bot in bots:
            if bot[2] == "R":
                stack.append(bot)
            else:
                next_bot = None
                while stack and healths[bot[3]] > 0:
                    next_bot = stack.pop()
                    
                    if healths[next_bot[3]] == healths[bot[3]]:
                        healths[next_bot[3]] = 0
                        healths[bot[3]] = 0
                    elif healths[next_bot[3]] > healths[bot[3]]:
                        healths[next_bot[3]] -= 1
                        healths[bot[3]] = 0
                    else:
                        healths[bot[3]] -= 1
                        healths[next_bot[3]] = 0

                if next_bot and healths[next_bot[3]] > 0:
                    stack.append(next_bot)

        out = []

        for h in healths:
            if h > 0:
                out.append(h)

        return out
        



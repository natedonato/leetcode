class Solution:
    def numberOfWays(self, corridor: str) -> int:
        start = 0
        seats = 0
        wall_opts = 0
        count = 1
        l = len(corridor)

        for e in corridor:
            if e == "S":
                seats += 1
                if seats < 2: 
                    continue
                if seats % 2 == 0:
                    wall_opts = 1
                else:
                    count *= wall_opts
                    wall_opts = 0
            elif e == "P" and seats > 1 and seats % 2 == 0:
                wall_opts += 1
        if seats % 2 == 0 and seats > 1:
            return count % 1_000_000_007
        return 0         

            
        

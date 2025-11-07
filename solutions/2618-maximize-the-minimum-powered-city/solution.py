class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        max_possible = k * len(stations) + sum(stations) + 1

        diff_array = [0] * len(stations)

        for idx, item in enumerate(stations):
            left = max(idx - r, 0)
            right = idx + r + 1

            diff_array[left] += item 
            if right < len(stations):
                diff_array[right] -= item

        self.diff_array = diff_array
        self.k = k
        self.r = r


        l = 0
        r = max_possible

        while l < r:
            mid = (r - l) // 2 + l

            if not self.canMakePower(mid):
                r = mid
            else:
                l = mid + 1
        
        return l - 1

            
                

    def canMakePower(self, target_power):
        diff_array = self.diff_array[:]
        k = self.k
        power = 0

        for index, d in enumerate(diff_array):
            power += d
            if power < target_power:
                delta = target_power - power
                if delta > k:
                    return False
                
                power = target_power
                right = index + self.r + self.r + 1
                if right < len(diff_array):
                    diff_array[right] -= delta

                k -= delta
        return True

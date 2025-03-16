class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        self.ranks = ranks
        self.cars = cars
        self.canRepairInTime(16)

        l = 0
        r = ranks[0] * (cars ** 2)

        while(l < r):
            mid = (r - l) // 2 + l
            outcome = self.canRepairInTime(mid)
            if(outcome == True):
                r = mid
            else:
                l = mid + 1

        return l


    def canRepairInTime(self, time):
        repairs = 0

        for mechanic in self.ranks:
            cars = math.floor( math.sqrt(time / mechanic ))
            repairs += cars
            if(repairs >= self.cars):
                return True

        return False

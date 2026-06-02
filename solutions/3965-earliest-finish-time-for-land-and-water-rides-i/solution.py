class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land_finish = math.inf
        for i in range(len(landStartTime)):
            min_land_finish = min(min_land_finish, landStartTime[i] + landDuration[i])

        min_finish = math.inf

        for i in range(len(waterStartTime)):
            start = max(min_land_finish, waterStartTime[i])
            min_finish = min(min_finish, start + waterDuration[i])

        min_water_finish = math.inf
        for i in range(len(waterStartTime)):
            min_water_finish = min(min_water_finish, waterStartTime[i] + waterDuration[i])
        

        for i in range(len(landStartTime)):
            start = max(min_water_finish, landStartTime[i])
            min_finish = min(min_finish, start + landDuration[i])

        return min_finish

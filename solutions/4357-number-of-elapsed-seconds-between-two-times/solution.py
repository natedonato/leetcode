class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def toSeconds(time):
            split = time.split(":")

            seconds = 0
            seconds += int(split[0]) * 60 * 60
            seconds += int(split[1]) * 60
            seconds += int(split[2])
            return seconds

        return toSeconds(endTime) - toSeconds(startTime)


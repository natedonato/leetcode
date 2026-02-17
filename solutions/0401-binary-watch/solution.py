class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.on = ["0"] * 10
        self.output = []
        self.btrack(0, turnedOn)

        self.output.sort()
        return self.output
    
    def parse(self):
        hours = "".join(self.on[0:4])
        minutes = "".join(self.on[4:])

        hours = int(hours,2)
        minutes = int(minutes,2)

        if hours < 12 and minutes < 60:
            hours = str(hours)
            minutes = str(minutes)
            while len(minutes) < 2:
                minutes = "0" + minutes

            self.output.append(hours+":"+minutes)

    def btrack(self, idx, count):
        if idx == len(self.on):
            if count == 0:
                self.parse()
            return

        # turn on
        if(count > 0):
            self.on[idx] = "1"
            self.btrack(idx + 1, count - 1)

        # leave off
        self.on[idx] = "0"
        self.btrack(idx + 1, count)

        return;

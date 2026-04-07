class Robot:
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    fdirs = ["East", "North", "West","South"]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0,0]
        self.dirIdx = 0
        self.turned = False

    def step(self, num: int) -> None:
        num %= 2 * self.width + 2 * self.height - 4
        if num == 0:
            num = 2 * self.width + 2 * self.height - 4

        for _ in range(num):
            next_pos = [self.pos[0] + self.dirs[self.dirIdx][0], self.pos[1] + self.dirs[self.dirIdx][1]]

            while next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= self.width or next_pos[1] >= self.height:
                self.dirIdx += 1
                self.dirIdx %= 4
                next_pos = [self.pos[0] + self.dirs[self.dirIdx][0], self.pos[1] + self.dirs[self.dirIdx][1]]

            self.pos = next_pos

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.fdirs[self.dirIdx]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

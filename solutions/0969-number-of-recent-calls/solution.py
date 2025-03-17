class RecentCounter:

    def __init__(self):
        self.q = deque()


    def ping(self, t: int) -> int:
        self.q.append(t)
        prev = t - 3000
        while self.q[0] < prev:
            self.q.popleft()

        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while True:
            if self.isBeautiful(n):
                return n
            n += 1


    def isBeautiful(self, n):
        s = str(n)
        c = Counter(s)

        for key, val in c.items():
            if int(key) != val:
                return False

        return True

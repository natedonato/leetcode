class Solution:
    
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        self.memo = {}
        self.mat = mat
        counts = Counter()
        best = -1

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                generated_numbers = self.makeNumbers(r,c)
                for num in generated_numbers:
                    if self.isPrime(num):
                        counts[num] += 1
                        if counts[num] == counts[best]:
                            best = max(num, best)
                        elif counts[num] > counts[best]:
                            best = num

        return best

    def isPrime(self, num):
        if num == 0:
            return False
        if num in self.memo:
            return self.memo[num]
        
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                self.memo[num] = False
                return False
        
        self.memo[num] = True
        return True

    def makeNumbers(self, r, c):
        nums = []
        n = len(self.mat)
        m = len(self.mat[0])
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                x = i
                y = j
                current_val = self.mat[r][c]
                while 0 <= r + x and r + x < n and 0 <= c + y and c + y < m:
                    current_val *= 10
                    current_val += self.mat[r+x][c+y]
                    nums.append(current_val)
                    x += i
                    y += j

        return nums





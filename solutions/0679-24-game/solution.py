class Solution:
    
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.solve(cards)

    def solve(self, arr):
        if len(arr) == 1:
            # print(arr)
            # print(24.001 > arr[0] and arr[0] > 23.999)
            return 24.001 > arr[0] and arr[0] > 23.999
        
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if i != j:
                    combos = self.combine(arr[i],arr[j])
                    rest = []
                    for k in range(0, len(arr)):
                        if k != i and k != j:
                            rest.append(arr[k])

                    for combo in combos:
                        if self.solve([combo] + rest) == True:
                            return True

        return False

    def combine(self, a,b):
        out = [a+b, a-b, a*b]
        if b != 0:
            out.append(a/b)
        return out


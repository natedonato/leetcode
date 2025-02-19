class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0

        def _btrack(arr):
            l = len(arr)
            if(l == n):
                self.count += 1
                if(self.count == k):
                    return ''.join(arr)
                else:
                    return ""

            last = ""
            if(l > 0):
                last = arr[-1]
            
            for char in "abc":
                if char != last:
                    arr.append(char)
                    result = _btrack(arr)
                    if(result != ""):
                        return result

                    arr.pop()
            
            return ""

        return _btrack([])

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ca = set()
        cb = set()
        p = 0

        out = []

        for i in range(len(A)):
            if A[i] == B[i]:
                p += 1
            else:
                ca.add(A[i])
                cb.add(B[i])

                if B[i] in ca:
                    p+= 1
                if A[i] in cb:
                    p+= 1
            out.append(p)

        return out

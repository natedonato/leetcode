class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        out = []
        min_dif = math.inf

        for i in range(len(arr) - 1):
            n1 = arr[i]
            n2 = arr[i+1]
            dif = n2 - n1

            if dif < min_dif:
                min_dif = dif
                out = [[n1, n2]]
            elif dif == min_dif:
                out.append([n1, n2])

        return out

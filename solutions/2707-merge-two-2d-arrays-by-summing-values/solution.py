class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        output = []
        idx1 = 0
        l1 = len(nums1)
        idx2 = 0
        l2 = len(nums2)

        while idx1 < l1 and idx2 < l2:
            first = nums1[idx1]
            second = nums2[idx2]

            if first[0] == second[0]:
                next_el = [first[0], first[1] + second[1]]
                output.append(next_el)
                idx1 += 1
                idx2 += 1
            elif first[0] < second[0]:
                output.append(first)
                idx1 += 1
            else:
                output.append(second)
                idx2 += 1

        while idx1 < l1:
            output.append(nums1[idx1])
            idx1 += 1

        while idx2 < l2:
            output.append(nums2[idx2])
            idx2 += 1

        return output

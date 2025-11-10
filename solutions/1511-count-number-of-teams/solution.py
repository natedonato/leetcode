from sortedcontainers import SortedList

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        left = SortedList()
        right = SortedList(rating)
        count = 0

        for n in rating:
            right.remove(n)

            smaller_left = left.bisect_left(n)
            larger_left = len(left) - left.bisect_right(n)
            smaller_right = right.bisect_left(n)
            larger_right = len(right) - right.bisect_right(n)

            count += smaller_left * larger_right
            count += smaller_right * larger_left

            left.add(n)

        return count

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1
        try:
            neg_index = next(i for i, e in enumerate(balance) if e < 0)
        except StopIteration:
            return 0
        neg_count = -balance[neg_index]

        i = 1
        move_count = 0
        while neg_count > 0:
            left = neg_index - i
            left %= len(balance)

            right = neg_index + i
            right %= len(balance)

            total = balance[left] + balance[right]

            num_to_move = min(total, neg_count)

            move_count += i * num_to_move
            neg_count -= num_to_move

            i += 1
        return move_count



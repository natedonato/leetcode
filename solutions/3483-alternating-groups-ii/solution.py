class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        alt_count = 0
        group_count = 0
        prev_color = colors[-1]
        l = len(colors)

        for i in range(0, l + k - 1):
            current_color = colors[i % l]

            if current_color != prev_color:
                alt_count += 1
            else:
                alt_count = 1

            if alt_count >= k:
                group_count += 1

            prev_color = current_color
            
        return group_count

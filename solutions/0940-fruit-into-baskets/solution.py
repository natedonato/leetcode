class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = {}
        left = 0
        total = 0
        for i in range(len(fruits)):
            next_tree = fruits[i]

            types[next_tree] = i
            if len(types) > 2:
                for t in types:
                    if t != next_tree and t != fruits[i - 1]:
                        left = types[t] + 1
                        del types[t]
                        break

            total = max(total, i - left + 1)

        return total 

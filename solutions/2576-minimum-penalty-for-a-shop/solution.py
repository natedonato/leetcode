class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customer_count = 0
        empty_cout = 0

        for c in customers:
            if c == "Y":
                customer_count += 1
            else:
                empty_cout += 1

        min_penalty = customer_count
        min_hour = 0
        current_penalty = customer_count

        for i, c in enumerate(customers):
            if current_penalty < min_penalty:
                min_hour = i
                min_penalty = current_penalty
            
            if c == "Y":
                current_penalty -= 1
            else:
                current_penalty += 1
            
        if current_penalty < min_penalty:
            min_hour = len(customers)
            
        return min_hour

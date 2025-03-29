class Solution:
    MOD = 10**9 + 7

    def maximumScore(self, nums: List[int], k: int) -> int:
        m = max(nums)
        l = len(nums)

        prime_scores = [0] * (m + 1)
        prime_scores[0] = 0
        for i in range(2, m+1):
            if prime_scores[i] == 0:
                prime_scores[i] = 1
                for j in range(i*2, m+1,i):
                    prime_scores[j] += 1

        left_indexes = [-1] * l
        right_indexes = [l] * l

        ## index, prime_score
        stack = []
        for i in range(0,l):
            current_score = prime_scores[nums[i]]

            while(stack and stack[-1][1] < current_score):
                top = stack.pop()
                top_index = top[0]
                right_indexes[top_index] = i
            
            if stack:
                left_indexes[i] = stack[-1][0]
            
            stack.append((i, current_score))

        num_subs = [0] * l

        for i in range(0,l):
            num_subs[i] = (right_indexes[i] -i) * (i - left_indexes[i])

        sorted_arr = []
        for i in range(0,l):
            sorted_arr.append((nums[i], num_subs[i]))

        sorted_arr.sort(reverse=True)
        print(sorted_arr)
        score = 1
        idx = 0
        while(k > 0):
            value = sorted_arr[idx][0]
            subarrays = sorted_arr[idx][1]
            next_ops = min(k, subarrays)
            
            score *= self.power(value, next_ops)
            score %= self.MOD
            k -= subarrays
            idx += 1

        return score 

    def power(self, base, exponent):
        output = 1
        while exponent > 0:
            if exponent % 2 == 1:
                output = (output * base) % self.MOD
            
            base = (base * base) % self.MOD
            exponent //= 2
        
        return output


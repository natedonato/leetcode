class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        products = defaultdict(int)
        l = len(nums)

        for i in range(0, l-1):
            for j in range(i+1, l):
                product = nums[i] * nums[j]
                products[product] += 1

        count = 0
        print(products)

        for key in products:
            val = products[key]
            combos_to_make_val = val * (val - 1) 
            count += 4 * combos_to_make_val

        return count


# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    leftproducts = [1]
    finalproducts = []
    
    i = 0
    while i < nums.length
        if(i != 0)
            leftproducts[i] = leftproducts[i-1] * nums[i-1]
        end
        i += 1
    end
    
    rightproduct = 1
    
    i = nums.length() - 1
    while(i >= 0)
        finalproducts[i] = leftproducts[i] * rightproduct
        rightproduct *= nums[i]
        i -= 1
    end
    
    return finalproducts
end
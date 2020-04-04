# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    i = 0
    zero_count = 0
    nonzero_count = 0
    while i < nums.length
        current_element = nums[i]
        if current_element == 0
            zero_count += 1    
        else
            nums[nonzero_count], nums[i] = nums[i], nums[nonzero_count]
            nonzero_count += 1
        end
        i += 1
    end
    return nums
end
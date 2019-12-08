# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    best = nums[0]
    curr_sum = 0
    
    nums.each do |num|
        curr_sum += num
        if(curr_sum > best)
            best = curr_sum
        end
        if curr_sum < 0
            curr_sum = 0
        end
    end
    return best
end
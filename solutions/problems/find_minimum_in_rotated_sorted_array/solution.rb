# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
    min = nums[0]
        
    nums.each do |num|
        if(num < min)
            return num
        end
    end
    
    return min
    
    
    
end
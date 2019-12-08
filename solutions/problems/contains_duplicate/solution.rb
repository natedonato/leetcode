# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    seen = Hash.new(false)
    
    nums.each do |num|
        if seen[num] == true
            return true
        else
            seen[num] = true
        end
    end
    
    return false
end
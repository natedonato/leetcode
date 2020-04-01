# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    seen = Hash.new(false)
    
    
    
    nums.each do |num|
        if(!seen[num])
            seen[num] = true
        elsif(seen[num])
            seen.delete(num)
        end
    end
    
    return seen.keys[0]
    
    
    
end
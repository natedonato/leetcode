# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}




def two_sum(nums, target)
    count = Hash.new(false)
    
    nums.each_with_index do |num, idx|
        difference = target - num
        if(count[difference] != false)
            return[count[difference], idx] 
        end
        count[num] = idx
    end
    
    
end
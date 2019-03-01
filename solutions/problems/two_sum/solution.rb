# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    
    nums.each.with_index do |n1, i1|
        nums.each.with_index do |n2, i2|
            if i1 < i2 && n1+n2 == target
                return [i1, i2]
            end
        end
    end          
    return nil
end
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    hash = {}
    nums.each_with_index do |num, idx|
        hash[num] = idx;
    end
    
    nums.each_with_index do |num, idx|
        pair = target - num
        if hash[pair] && hash[pair] != idx
            return [hash[pair], idx]
        end
    end
end
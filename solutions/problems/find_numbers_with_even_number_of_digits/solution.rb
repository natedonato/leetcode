# @param {Integer[]} nums
# @return {Integer}
def find_numbers(nums)
    count = 0
    nums.each do |num|
        count += 1 if even_num_digits?(num) 
    end
    return count 
    
    


end

def even_num_digits?(num) 
    return num.to_s.length % 2 == 0
end
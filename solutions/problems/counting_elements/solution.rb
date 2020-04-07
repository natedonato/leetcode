# @param {Integer[]} arr
# @return {Integer}
def count_elements(arr)
    count = Hash.new{0}
    total = 0
    
    arr.each do |n|
        count[n] += 1
    end
    
    count.keys.each do |key|
        if count[key + 1] > 0
            total += count[key] 
        end
    end
    
    return total
end
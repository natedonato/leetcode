# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    hash = {} 
    
    strs.each do |str|
        sorted = str.split(''). sort().join('')
        
        
        if !hash[sorted]
            hash[sorted] = [] 
        end
        hash[sorted].push(str)
    end
    
    
    
    return hash.values
    
    
end
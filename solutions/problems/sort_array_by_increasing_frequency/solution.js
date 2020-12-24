/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
    let counts = {};
    for(const num of nums){
        if(!counts[num]){
            counts[num] = 1;
        }else{
            counts[num] += 1;
        }
    }
    
    return nums.sort((a,b) => counts[a] === counts[b] ? b - a : counts[a] - counts[b])

};
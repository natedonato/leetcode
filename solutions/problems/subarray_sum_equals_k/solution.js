/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let curr_sum = 0;
    let map = {0: 1};
    let count = 0;
    
    for(let i = 0; i < nums.length; i++){
        curr_sum += nums[i];
        
        if(map[curr_sum-k] !== undefined){
            count += map[curr_sum-k]            
        }
        
        if(map[curr_sum] === undefined){
            map[curr_sum] = 1
        }else{
            map[curr_sum] += 1;
        }
    }
    console.log(map)
    
    return count
};
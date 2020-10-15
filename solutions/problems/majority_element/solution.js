/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = {};
    let target = nums.length / 2;
    
    
    
    
    for(const num of nums){
        if(!count[num]){
            count[num] = 1
        }else{
            count[num] += 1;
   
        };
        if(count[num] >= target){
            return num;
        };
    }
};
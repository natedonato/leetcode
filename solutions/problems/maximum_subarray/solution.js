/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
   let sum = -Infinity;
   let largest = -Infinity;
    
    for(let i = 0; i < nums.length; i++){
        if(nums[i] > sum + nums[i]){
            sum = 0
        }
        sum += nums[i];
        largest = Math.max(sum, largest)
    }
    return largest;
};
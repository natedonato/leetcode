/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumGap = function(nums) {
    if(nums.length < 2){return 0};
    nums = nums.sort((a,b)=> a - b);
    let dif = nums[1] - nums[0];
    
    for(let i = 1; i < nums.length; i++){
        if(nums[i] - nums[i - 1] > dif){
            dif = nums[i] - nums[i - 1]
        }   
    };
    
    return dif;
};
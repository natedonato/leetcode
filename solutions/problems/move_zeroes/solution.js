/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let pointer = 0;
    let i = 0;
    
    while(i < nums.length){
        if(nums[i] === 0){
            i++;
        }else {
            if(pointer !== i){
                [nums[i], nums[pointer]] = [nums[pointer], nums[i]]
            }
            i++;
            pointer++;
        }
    }
};
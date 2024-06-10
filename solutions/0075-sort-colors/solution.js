/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for(let i = 0; i < nums.length; i++){
        let minIdx = i;
        for(let j = i; j < nums.length; j++){
            if(nums[minIdx] > nums[j]){
                minIdx = j;
            }
        }
        
        [nums[i],nums[minIdx]] = [nums[minIdx],nums[i]];
    }
};

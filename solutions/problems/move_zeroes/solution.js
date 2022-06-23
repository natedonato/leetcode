/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let nextSlot = 0;
    let currPointer = 0;
    
    while(currPointer < nums.length){
        const nextVal = nums[currPointer];
        
        if(nextVal===0){
            currPointer += 1;
        }else{
            [nums[nextSlot], nums[currPointer]] = [nums[currPointer], nums[nextSlot]];
            nextSlot+=1;
            currPointer += 1;
        };
    }    
};
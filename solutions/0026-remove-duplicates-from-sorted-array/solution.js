/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0;
    let current = null;
    
    for(let j = 0; j < nums.length; j++){
        if(nums[j] !== current){
            current = nums[j]
            nums[i] = current;
            i++;
        }
    }
    
    return i;
};

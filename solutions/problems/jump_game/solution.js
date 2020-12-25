/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let current = 0;
    let remaining = nums[0];
    
    while(remaining > 0){
        current += 1;
        remaining -= 1;
        if(nums[current] > remaining){
            remaining = nums[current];
        }
    }
    return (current >= nums.length - 1)
};
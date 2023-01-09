/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = 0;
    let majority = null;

    for(let i = 0; i < nums.length; i++){
        if(count === 0){
            majority = nums[i]
            count += 1;
        }else if(nums[i] === majority){
            count += 1;
        }else if(nums[i] !== majority){
            count -= 1;
        }
    }

    return majority;
};
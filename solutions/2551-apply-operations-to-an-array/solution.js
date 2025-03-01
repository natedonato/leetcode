/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
    const output = new Array(nums.length).fill(0);
    let out_index = 0;

    for(let i = 0; i < nums.length; i++){
        if(nums[i] === nums[i+1]){
            nums[i] = nums[i] * 2;
            nums[i + 1] = 0;
        }

        if(nums[i] !== 0){
            output[out_index] = nums[i];
            out_index += 1;
        }
    }

    return output;
};

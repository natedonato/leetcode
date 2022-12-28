/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let runningProduct = 1;
    
    let output = [1];
    for(let i = 1; i < nums.length; i++){
        runningProduct *= nums[i-1];
        output.push(runningProduct);
    }
    runningProduct = 1;
    for(let i = nums.length - 2; i >= 0; i--){
        runningProduct *= nums[i+1];
        output[i] *= runningProduct
    }
    
    return output;
};
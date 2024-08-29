/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let product = 1;
    let output = new Array(nums.length).fill(1);    
    
    for(let i = 0; i < nums.length - 1; i++){
        product *= nums[i]
        output[i + 1] = product;
    }
    
    console.log(output);
    
    product = 1;
    
    for(let i = nums.length - 1; i > 0; i--){
        product *= nums[i];
        output[i - 1] *= product;
    }
    
    return output;
};

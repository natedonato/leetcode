/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let prod = 1;
    let arr = []
    
    for(let i = nums.length - 1; i >= 0; --i){
        arr[i] = prod;
        prod *= nums[i];
    }
    
    prod = 1;
    
    for(let i = 0; i < nums.length; ++i){
        arr[i] = arr[i] * prod;
        prod *= nums[i]
    }
    
    return arr
};
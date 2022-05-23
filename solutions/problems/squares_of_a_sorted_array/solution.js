/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    let length = 0;
    
    let output = new Array(nums.length).fill(null);
    
    while(length < nums.length){
        let leftVal = nums[left] * nums[left];
        let rightVal = nums[right] * nums[right];
        
        if(leftVal > rightVal){
            output[nums.length - 1 - length] = leftVal;
            left += 1
        }else{
            output[nums.length - 1 - length] = rightVal;
            right -= 1;
        }
        
        length += 1;
    }
    
    return output;
};
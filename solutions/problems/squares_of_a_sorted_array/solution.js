/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let output = [];
    
    let left = 0;
    let right = nums.length -1;
    while(left <= right){
        if(nums[left]*nums[left] >= nums[right] *nums[right]){
            output.unshift(nums[left]*nums[left]);
            left += 1;
        }else{
            output.unshift(nums[right]*nums[right]);
            right -=1;
        }
    }
    
    return output;
};
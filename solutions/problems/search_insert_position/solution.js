/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    
    while (left <= right){
        const mid = Math.floor((right - left) / 2) + left;
        const val = nums[mid];
        
        if(val < target){
            left = mid + 1
        }else if(val > target){
            right = mid - 1;
        }else if (val === target){
            return mid;
        }
    }
    
    return left
};
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while(left <= right){
        let mid = Math.floor((right - left) / 2) + left;
        let val = nums[mid];
        
        if(val === target){
            return mid;
        }else if (val > target){
            right = mid - 1;
        }else{
            left = mid + 1;
        }
    }
    
    return -1
};
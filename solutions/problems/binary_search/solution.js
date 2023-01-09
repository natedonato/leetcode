/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {

    let left = 0;
    let right = nums.length - 1;

    while(left < right){
        mid = left + Math.floor((right - left) / 2);

        if(nums[mid] >= target){
            right = mid
        }else{
            left = mid + 1;
        }
    }

    if(nums[left] === target){
        return left
    }else{
        return -1
    }
};
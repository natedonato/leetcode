/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    let times = k % nums.length;
    
    for(let i = 0; i < times; i++){
        nums.unshift(nums.pop());
    }
    return nums;
};
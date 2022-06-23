/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k % nums.length;
    
    reverseSection(nums, 0, nums.length-1);
    reverseSection(nums, 0, k-1);
    reverseSection(nums,k, nums.length-1)
    
};

// reverses section of array inclusive of endpoints in place
var reverseSection = function(nums,i,j) {
    while(i < j){
        [nums[i],nums[j]] = [nums[j], nums[i]];
        i++;
        j--;
    }
};

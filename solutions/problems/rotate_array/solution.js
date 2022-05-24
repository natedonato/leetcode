/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k % nums.length;
    reverseSection(nums, 0, nums.length-1);
    reverseSection(nums, 0, k-1);
    reverseSection(nums, k, nums.length-1);    
};

// inclusive of endpoint
var reverseSection = function(arr, start, end){
    while(start <= end){
        [arr[start],arr[end]] = [arr[end], arr[start]];
        start++;
        end--;
    }
}
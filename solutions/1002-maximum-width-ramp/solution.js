/**
 * @param {number[]} nums
 * @return {number}
 */
var maxWidthRamp = function(nums) {
    const maxRight = new Array(nums.length);
    const n = nums.length;
    let max = nums[n - 1];
    for(let i = 0; i < n; i++){
        j = n - 1 - i;
        const num = nums[j];
        max = Math.max(max, num);
        maxRight[j] = max;
    }
    
    let l = 0;
    let r = 0;
    let width = 0;
    
    while(r < nums.length){
        while(l < r && nums[l] > maxRight[r]){
            l += 1;
        }
        width = Math.max(width, r - l);
        r += 1
    };
    
    return width;
};

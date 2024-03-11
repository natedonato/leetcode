/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length -1;
    const condition = (val) => {
        return val >= target;
    }
    
    
    while(left < right){
        const mid = Math.floor((right - left) / 2) + left;
        const val = nums[mid]
        
        if(condition(val)){
            right = mid;
        }else{
            left = mid + 1;
        }
    }

    console.log(left);
    return (nums[left] === target ? left : -1) ;
};

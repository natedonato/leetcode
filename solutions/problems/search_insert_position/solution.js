/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    const cond = (idx) => {
        if(nums[idx] >= target){
            return true;
        }
        return false;
    }
    
    let [left,right] = [0, nums.length];
    
    while(left < right){
        let mid = left + Math.floor((right -left)/2);
        
        if(cond(mid)){
            right = mid;
        }else{
            left = mid + 1;
        }
    }

    return left
};
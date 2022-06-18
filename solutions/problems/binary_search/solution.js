/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let condition = (value) =>{
        if(value >= target){
            return true   
        }else{
            return false
        }
    }
    
    let left = 0
    let right = nums.length - 1;
    
    while(left < right){
        let mid = left + Math.floor((right - left)/2);
        let val = nums[mid];
        
        if(condition(val)){
            right = mid;   
        }else{
            left = mid + 1;
        }
    }
    return(nums[left] === target ? left : -1);
};
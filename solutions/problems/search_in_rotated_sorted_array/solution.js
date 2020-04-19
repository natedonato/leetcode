/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0;
    let r = nums.length - 1;
    
    while(l <= r){
        let midpoint = Math.floor((l + r) / 2);
        let midval = nums[midpoint];
        
        if(nums[l] < nums[r]){
            if(target < midval){
                r = midpoint - 1
            }else if(target > midval){
                l = midpoint + 1
            }else{
                return midpoint;
            }
        }else if(target < midval){
            if((nums[l] < midval && nums[l] <= target) || nums[l] > midval){
                r = midpoint - 1;
            }else{
                l = midpoint + 1
            }
        }else if(target > midval){
            if((nums[r] > midval && nums[r] >= target) || (nums[r] <= midval)){
                l = midpoint + 1;
            }else{
                r = midpoint - 1 
            }
        }else if(target === midval){
            return midpoint;
        }else if(l === r){
            return -1
        }
    }
        
    return nums[l] === target ? l : -1
};
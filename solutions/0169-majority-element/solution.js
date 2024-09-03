/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let currentEl = nums[0];
    let count = 1;
    
    for(let i = 1; i < nums.length; i++){
        const next = nums[i]
        if(next === currentEl){
            count += 1;
        }else{
            count -= 1;
            if(count === 0){
                currentEl = next;
                count = 1;
            }
        }
        
    }
    return currentEl; 
};

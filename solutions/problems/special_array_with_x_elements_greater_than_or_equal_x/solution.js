/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
  for(let i = 0; i < nums.length; i++){
    let count = 0;
    for(let j = 0; j < nums.length; j++){
        if(nums[j] >= i + 1){
            count += 1;
        }
    }   
    if(count === i+1){
        return i + 1;
    }
  }
  return -1
};
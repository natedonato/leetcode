/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let minJumps = [0];
    for(let i = 0; i < nums.length; i++){
        let nextJumps = minJumps[i] + 1;
        let currentReach = nums[i];
        for(let j = 0; j <= currentReach; j++){
            if(minJumps[i + j] === undefined || nextJumps < minJumps[i + j]){
                minJumps[i + j] = nextJumps;
            }      
        }
    }
    return minJumps[nums.length - 1]
};
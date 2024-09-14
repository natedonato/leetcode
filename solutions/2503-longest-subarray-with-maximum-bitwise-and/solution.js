/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let max = 0;
    let maxRun = 0;
    let currentRun = 0;

    for(const num of nums){
        if(num > max){
            max = num;
            maxRun = 1;
            currentRun = 1;
        }else if(num === max){
            currentRun += 1;
            if(currentRun > maxRun){
                maxRun = currentRun
            }
        }else{
            currentRun = 0
        }

    }
    
    return maxRun;
};

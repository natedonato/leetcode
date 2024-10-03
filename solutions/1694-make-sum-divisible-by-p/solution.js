/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minSubarray = function(nums, p) {
    let sum = 0;

    for(const num of nums){
        sum += num;
    }
    
    let target = sum % p;
    if(target === 0){
        return 0;
    }
    
    const modMap = new Map();
    modMap.set(0, -1);
    let currentSum = 0;
    let minLen = nums.length;
    
    for(let i = 0; i < nums.length; i++){
        const num = nums[i];
        currentSum += num;
        currentSum %= p;
        const dif = (currentSum - target + p) % p;
        if(modMap.has(dif)){
            minLen = Math.min(minLen, i - modMap.get(dif))
        }
        modMap.set(currentSum, i);
        
    }
    
    if(minLen === nums.length){
        return -1
    };
    
    return minLen;
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const firstSeen = new Map();
    
    for(let i = 0; i < nums.length; i++){
        
        let compliment = target - nums[i];
        if(firstSeen.get(compliment) !== undefined){
            return [firstSeen.get(compliment), i];
        }else{
            firstSeen.set(nums[i], i)
        }
    }
};

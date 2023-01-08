/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {};

    for(let i = 0; i < nums.length; i++){
        let dif = target - nums[i];

        if(map[dif] !== undefined){
            return [i,map[dif]]
        }else{
            map[nums[i]] = i;
        }
    }
};
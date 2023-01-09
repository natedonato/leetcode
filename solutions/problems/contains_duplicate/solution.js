/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let seen = {};

    for(const num of nums){
        if(seen[num]){
            return true
        }else{
            seen[num] = true;
        }
    }

    return false;
};
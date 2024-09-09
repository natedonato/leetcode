/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let last = 0;

    for(const num of nums){
        last = last ^ num;
    }

    return last;
};

/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    const left = [];
    const mid = [];
    const right = [];
    for(const num of nums){
        if(num < pivot){
            left.push(num)
        }else if (num === pivot){
            mid.push(num)
        }else{
            right.push(num)
        }
    }

    return left.concat(mid).concat(right);
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSneakyNumbers = function(nums) {
    const output = [];
    const set = new Set();
    for(const num of nums){
        if(set.has(num)){
            output.push(num)
        }else{
            set.add(num)
        }
    }
    return output;
};

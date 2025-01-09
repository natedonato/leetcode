/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let l = 0;
    let r = numbers.length - 1;
    let sum = numbers[l] + numbers[r];
    while(sum !== target){
        if(sum > target){
            r -= 1;
        }else{
            l += 1
        }
        sum = numbers[l] + numbers[r]
    }

    return [l + 1,r + 1]
};

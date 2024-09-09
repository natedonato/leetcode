/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    let sum = 0;
    let num = 0;
    for(const e of nums){
        if(e % 3 === 0 && e % 2 === 0){
            sum += e;
            num += 1;
        }
    }
    
    if(num === 0){
        return 0;
    }
    return (Math.floor(sum/num));
};

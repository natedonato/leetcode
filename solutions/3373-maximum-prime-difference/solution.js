/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumPrimeDifference = function(nums) {
    let min_idx = -1;
    let max_idx = -1;
    const cache = new Map();


    for(let i = 0; i < nums.length; i++){
        const num = nums[i];
        if(!cache.has(num)){
            cache.set(num, isPrime(num));
        }

        if(cache.get(num) === true){
            if(min_idx === -1){
                min_idx = i;
            }

            max_idx = i
        }
    }

    return max_idx - min_idx;
};

function isPrime(num){
    if(num === 1){
        return false;
    }
    const root = Math.sqrt(num)
    for(let i = 2; i <= root; i++){
        if(num % i === 0){
            return false;
        }
    }

    return true;
}

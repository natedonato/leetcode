/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const digitSums = {};
    for(const num of nums){
        sum = sumDigits(num);
        if(!digitSums[sum]){
            digitSums[sum] = [num]
        }else{
            digitSums[sum].push(num);
        }

        digitSums[sum] = digitSums[sum].sort((a,b) => b - a).slice(0, 2)
    }

    let max = -1

    for(const arr of Object.values(digitSums)){
        if(arr.length < 2){
            continue
        }else{
            max = Math.max(max, (arr[0] + arr[1]))
        }
    }

    return max
};

function sumDigits(num){
    sum = 0;
    while(num > 0){
        sum += num % 10;
        num = Math.floor(num / 10);
    }

    return sum
};

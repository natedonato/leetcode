/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    let counts = {};

    for(const char of s){
        counts[char] = (counts[char] || 0) + 1;
    }

    let l = 0;
    let sum = 0;

    for(let num of Object.values(counts)){
        sum += num;
        num -= num % 2;
        l += num;
    }

    if(sum > l){
        l += 1;
    }

    return l
};
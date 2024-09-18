/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let i = digits.length - 1;
    digits[i] += 1;
    
    while(digits[i] >= 10 && i >= 1){
        digits[i - 1] += 1;
        digits[i] = digits[i] % 10;
        i -= 1;
    }
    
    if(digits[0] >= 10){
        digits[0] = digits[0] % 10;
        digits.unshift(1);
    }
    
    return digits;
};

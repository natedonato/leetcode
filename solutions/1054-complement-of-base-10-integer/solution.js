/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function(n) {
    if(n === 0){
        return 1
    }

    let ones = 0
    while(ones < n){
        ones = (ones << 1) + 1
    }

    return n ^ ones
};

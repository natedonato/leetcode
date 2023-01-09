/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    a = a.split('').reverse();
    b = b.split('').reverse();
    let res = '';
    let carry = 0;

    for(let i = 0; i < Math.max(a.length, b.length); i++){
        let next = +(a[i] || 0) + +(b[i] || 0) + carry;

        if(next > 1){
            carry = 1;
        }else{
            carry = 0;
        }
        next = next % 2;
        res += next;
    }

    if(carry){
        res += carry
    }
    return res.split('').reverse().join('')
};
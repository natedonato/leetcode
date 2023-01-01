/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let output = 0;
    n = n.toString(2);
    
    for(let i = 0; i < n.length; i++){
        if(n.charAt(i) === '1'){
            output += 1;
        }
    }
    
    return output;
};
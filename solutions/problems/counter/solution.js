/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n - 1;
    return () =>{
        count += 1;
        return count;
    };
};
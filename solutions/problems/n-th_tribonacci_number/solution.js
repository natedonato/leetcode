/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n, memo) {
    if(!memo){
        memo = {
        '0': 0,
        '1': 1,
        '2': 1,
        };
    }
    
    if(memo[n] !== undefined){
        return memo[n]
    };
    
    let next = tribonacci(n-1, memo) + tribonacci(n-2, memo) + tribonacci(n-3, memo);
    memo[n] = next;
    return next;
};
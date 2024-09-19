/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let prev1 = 1;
    let prev2 = 1;
    let next = 1;
    
    for(let i = 2; i <= n; i++){
        next = prev1 + prev2;
        prev1 = prev2; 
        prev2 = next;
    }
    
    return next;
};

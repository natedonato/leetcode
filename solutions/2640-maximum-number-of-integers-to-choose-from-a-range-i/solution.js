/**
 * @param {number[]} banned
 * @param {number} n
 * @param {number} maxSum
 * @return {number}
 */
var maxCount = function(banned, n, maxSum) {
    const b = new Set(banned);
    
    let count = 0;
    let sum = 0;
        
    for(let i = 1; i <= n; i++){
        if(!b.has(i)){
            if(sum + i <= maxSum){
                sum += i;
                count += 1;
            }   
        }
    }
    
    return count;
};

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthFactor = function(n, k) {
    const facts = [];
    
    for(let i = 1; i <= n; i++){
        if(n % i === 0){
            facts.push(i);
            if(facts.length === k){
                return facts.pop();
            }
        }
    }
    
    return -1;
};

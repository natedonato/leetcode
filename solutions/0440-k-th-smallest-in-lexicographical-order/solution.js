/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(n, k) {
    let current = 1;
    k -= 1;

    while(k > 0){
        let step = getSteps(n, current, current + 1);
        if(step <= k){
            current += 1;
            k -= step;
        }else{
            current *= 10;
            k -= 1;
        }
        
    }

    return current;

    function getSteps(n, p1, p2){
        let steps = 0;
        while(p1 <= n){
            steps += Math.min(n + 1, p2) - p1;
            p1 *= 10;
            p2 *= 10;      
        }
        return steps;
    }
};

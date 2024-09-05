/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
// sum (rolls) + sum (n) / (m + n) = mean

var missingRolls = function(rolls, mean, n) {
    let total = mean * (n + rolls.length);
    let sumRolls = rolls.reduce((acc,el) => acc + el,0)
    let totalMissing = total - sumRolls;
    
    if(totalMissing < n || totalMissing > 6 * n){
        return [];
    }
    
    
    const output = new Array(n).fill(1);
    
    totalMissing -= n;
    let greedy = Math.floor(totalMissing / 5);
    let leftover = totalMissing % 5;
    
    for(let i = 0; i < greedy; i++){
        output[i] = 6;
    }
    
    if(leftover){
        output[greedy] += leftover;
    }
    
    return output;
};

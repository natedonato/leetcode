/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
var construct2DArray = function(original, m, n) {
    if(m * n !== original.length){
        return [];
    }
    
    const output = new Array(m).fill(0).map(el => new Array(n));
    
    for(let i = 0; i < original.length; i++){
        output[Math.floor(i / n)][i % n] = original[i]
    }
    
    return output;
};

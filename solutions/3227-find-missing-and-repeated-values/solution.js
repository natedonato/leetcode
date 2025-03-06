/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    const seen = new Set()
    let a, b = null

    for(const row of grid){
        for(const el of row){
            if(!seen.has(el)){
                seen.add(el)
            }else{
                a = el
            }
        }
    }

    for(let i = 1; i <= grid.length ** 2; i++){
        if(!seen.has(i)){
            b = i
            return [a,b]
        }
    }
};

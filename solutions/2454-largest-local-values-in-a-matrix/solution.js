/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var largestLocal = function(grid) {
    const output = new Array(grid.length - 2).fill(0).map(el => new Array(grid.length - 2));
    
    for(let i = 0; i < output.length; i++){
        for(let j = 0; j < output.length; j++){
            output[i][j] = getLocalMax(i+1, j+1)   
        }
    }
    
    
    
    return output;
    
    function getLocalMax(i,j){
        let max = 0;
        for(let r = -1; r <= 1; r++){
            for(let c = -1; c <= 1; c++){
                max = Math.max(grid[r + i][c + j], max)
            }
        }
        return max;
    }
};

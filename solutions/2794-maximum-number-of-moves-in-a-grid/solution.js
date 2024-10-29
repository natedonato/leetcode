/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxMoves = function(grid) {
    const memo = {};
    
    function solve(prev, i, j){
        const key = [i,j].join(";")
        if(memo[key]){
            return memo[key]
        }
        if(i < 0 || j < 0 || i >= grid.length || j >= grid[0].length){
            return 0;
        }
        
        const current = grid[i][j];
        
        if(current <= prev){
            return 0;
        }
        
        let best = Math.max(
            solve(current,i-1, j+1),
            solve(current,i, j+1),
            solve(current,i+1, j+1)
        ) + 1
        
        memo[key] = best;
        return best;
    }
    
    let best = 0;
    for(let i = 0; i < grid.length; i++){
        best = Math.max(best, solve(0, i, 0));
    }
    
    return best - 1;
};

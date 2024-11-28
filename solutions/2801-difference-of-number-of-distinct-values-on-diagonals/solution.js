/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var differenceOfDistinctValues = function(grid) {
    const ans = new Array(grid.length).fill(0).map(el => new Array(grid[0].length));
    
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[0].length; j++){
            ans[i][j] = Math.abs(leftAbove(i,j,grid) - rightBelow(i,j,grid));
        }
    }
    
    return ans;
};

function leftAbove(x,y,grid){
    const s = new Set();
    
    while(x > 0 && y > 0){
        x -= 1;
        y-= 1;
        s.add(grid[x][y]);
    }
    return s.size;
}

function rightBelow(x,y,grid){
    const s = new Set();
    while(x < grid.length - 1 && y < grid[0].length - 1){
        x += 1;
        y += 1;
        s.add(grid[x][y])
    }
    return s.size;
}

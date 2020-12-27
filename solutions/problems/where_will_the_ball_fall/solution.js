/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function(grid) {    
    let output = []
    for(let i = 0; i < grid[0].length; i++){
        output.push(drop(i, grid));
    }
    return output
};

var drop = function(column, grid){
    let [row,col] = [0, column];

    while(row < grid.length){
        let current = grid[row][col];
        if(current === 1){
            col += 1
            if(grid[row][col] === undefined || grid[row][col] === -1){
                return -1
            }
        }else{
            col -= 1;
            if(grid[row][col] === undefined || grid[row][col] === 1){
                return -1
            }
        }
        row += 1;
    }
    return col;
}
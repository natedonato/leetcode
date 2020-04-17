/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let explored = new Array(grid.length).fill(undefined).map(()=> new Array(grid[0].length).fill(undefined));
    
    let count = 0;
    
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[0].length; j++){
            if(explored[i][j] == undefined){
                explored[i][j] = true;
                let val = grid[i][j]
                if (val !== '0'){
                    count += 1;
                    exploreIsland(i,j, explored, grid)
                } 
            }    
        }
    }        
    return count;
};



var exploreIsland = function(i,j,explored, grid){
    let queue = [[i,j]];
    
    while(queue.length > 0){
        
        let [x,y] = queue.shift();
        
        let left = [x-1, y];
        let right = [x+1, y];
        let up = [x, y+1];
        let down = [x, y-1];
        
        [left,right,up,down].forEach(point => {
            if(point[0] < 0 || point[1] < 0 || point[0] >= grid.length || point[1] >= grid[0].length){
            }else if(!explored[point[0]][point[1]]){
                explored[point[0]][point[1]] = true;
                if(grid[point[0]][point[1]] !== '0'){
                    queue.push(point)
                }
            }
        })
    }
}



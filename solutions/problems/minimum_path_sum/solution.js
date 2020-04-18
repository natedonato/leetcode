/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    let sums = new Array(m).fill(null).map(()=>new Array(n).fill(null));
    sums[0][0] = grid[0][0];
    
    queue=[[0,0]];
    
    while(queue.length > 0){
        let [x,y] = queue.shift();
        let current_sum = sums[x][y];
        
        if(x + 1 < m){
            x += 1;
            if(sums[x][y] === null){
                sums[x][y] = current_sum + grid[x][y];
                queue.push([x,y]);
            }else if(sums[x][y] > current_sum + grid[x][y]){
                sums[x][y] = current_sum + grid[x][y];
            }
            x -= 1;
        }
    
         
        if(y + 1 <= n){
            y += 1;
            if(sums[x][y] === null){
                sums[x][y] = current_sum + grid[x][y];
                queue.push([x,y]);
            }else if(sums[x][y] > current_sum + grid[x][y]){
                sums[x][y] = current_sum + grid[x][y];
            }
        }
    }
    return sums[m-1][n-1]
};
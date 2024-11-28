/**
 * @param {number[][]} grid
 * @return {number}
 */
function compare(a,b){
    return (a[1] - b[1]);
}


var minimumObstacles = function(grid) {
    // [ [x,y], wallsCrossed]
    const mpq = new PriorityQueue({compare: compare});
    const visited = new Set();
    
    mpq.enqueue([[0,0],0]);
    
    while(mpq.size() > 0){
        const next = mpq.dequeue();
        const [x,y] = next[0];
        const key = [x,y].join(",")
        
        let walls = next[1];
        
        if(visited.has(key)){
            continue;    
        }else{
            visited.add(key)
        }
        
        if(x === grid.length - 1 && y === grid[0].length - 1){
            return walls;
        };
                
        if(grid[x][y] === 1){
            walls += 1;
        }
        
   
        for(const el of [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]){
            
            if(!(el[0] < 0 || el[0] >= grid.length || el[1] < 0 || el[1] >= grid[0].length)){
                mpq.enqueue([[el[0],el[1]],walls]);
            }   
        }
    }
};



/// bfs / dijkstras 

// keep track of visited
// maintain current number of walls crossed
// do dijkstras with priority queue


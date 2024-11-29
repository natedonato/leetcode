/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumTime = function(grid) {
    if(grid[0][1] > 1 && grid[1][0] > 1){
        return -1;
    }
    
    const q = new PriorityQueue({compare: 
        (a,b) => a[1] - b[1]                    
    });
    
    const visited = new Set();
    q.enqueue([[0,0],0]);
    
    //[[x,y],currentTime];
    while(q.size() > 0){
        const current = q.dequeue();
        let [[x,y], currentTime] = current;
        const key = current[0].join(",");
        
        if(visited.has(key)){
            continue;
        }else{
            visited.add(key);
        }
                
        if(x === grid.length - 1 && y === grid[0].length -1){
            return currentTime;
        }
        
        currentTime += 1;
        
        for(const [nextX, nextY] of [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]){
            if(nextX >= 0 && nextY >= 0 && nextX < grid.length && nextY < grid[0].length){
                nextTime = Math.max(grid[nextX][nextY],currentTime);
                
                if(nextTime > currentTime){
                    if((nextTime - currentTime) % 2 === 1){
                        nextTime += 1;
                    }
                }
                
                q.enqueue([[nextX, nextY],nextTime]);
            }
        }
    }
};



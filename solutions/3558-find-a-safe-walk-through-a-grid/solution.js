/**
 * @param {number[][]} grid
 * @param {number} health
 * @return {boolean}
 */
var findSafeWalk = function(grid, health) {
    
    // Set<`${x},${y}`> = best seen HP value at that cell
    const seen = new Set();
    
    // Get our BFS ready
    let start = [0,0,health];
    const queue = [start];
    
    while(queue.length > 0){
        
        // get current cell coordinates and current HP 
        let node = queue.shift();
        let [x,y,health] = node;
        
        // update our health using current grid cell value
        health -= grid[x][y];
                
        // if dead at the current cell, continue to next node in queue
        if(health <= 0){
            continue;
        }
        
        // if not dead and at the finish point, return true;
        if(x === grid.length - 1 && y === grid[0].length - 1){
            return true;
        }
        
        // check if we've already visited this cell at an equal or better HP value
        // if we've already visited this cell with eqal or better HP value, continue
        // else we mark current cell as visited with our current HP value
        let coord = `${x},${y}`
        if(seen[coord] >= health){
            continue;
        }else{
            seen[coord] = health;
        }
        
        // Get neighboring cells and add to BFS queue with our current HP value 
        const neighbors = getValidNeighbors(x,y);
        for(const child of neighbors){
            const [x,y] = child;
            queue.push([x,y,health]);
        }
    }
    
    // If we exhausted the BFS queue and didn't reach the end with positive HP, can finally return false
    return false;
    
    
    // helper function to get neighboring cells within the grid bounds
    
    function getValidNeighbors(x,y){
        
        let coords = [];
        
        // vectors to move up, down, left, and right
        const offsets = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]
        
        for(const offset of offsets){
            // Use our vectors to get the neighboring coordinates
            x1 = x + offset[0];
            y1 = y + offset[1];
            
            // If both the X and Y coordinate are within bounds, we can add it to the helper function output 
            if(x1 >= 0 && y1 >= 0 && x1 < grid.length && y1 < grid[0].length){
                coords.push([x1,y1]);
            }
        }
        
        return coords;
    }
};



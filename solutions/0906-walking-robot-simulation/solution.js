/**
 * @param {number[]} commands
 * @param {number[][]} obstacles
 * @return {number}
 */
var robotSim = function(commands, obstacles) {
    let position = [0,0];    
    let max = 0;
    const rocks = new Map();
    
    const vectors = [
        [0,1], //n
        [1,0], //e
        [0,-1],//s
        [-1,0] //w
    ]
    
    let currentDir = 0;
    
    for(const rock of obstacles){
        if(!rocks[rock[0]]){
            rocks[rock[0]] = new Set();
        }
        rocks[rock[0]].add(rock[1]);
    };
    
    for(const command of commands){
        if(command === -1){
            currentDir = currentDir + 1
            currentDir %= 4;
        }else if (command === -2){
            currentDir = currentDir - 1;
            if(currentDir === -1){
                currentDir = 3;
            }
        }else{
            for(let i = 0; i < command; i++){
                const nextX = position[0] + vectors[currentDir][0];
                const nextY = position[1] + vectors[currentDir][1];
                if(rocks[nextX] && rocks[nextX].has(nextY)){
                    break;
                }else{
                    position = [nextX, nextY];
                    max = Math.max(position[0]**2 + position[1] **2, max);
                }
            }   
        }
    }

    return max;
};

/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    let queue = [start];
    let visited = {};
    
    while(queue.length > 0){
        let current = queue.pop();
        let value = arr[current];
        
        if(value === 0){
            return true;
        }
        visited[current] = true;
        
        
        for(const next of [current + value, current - value]){
            if(visited[next] === undefined){
                queue.push(next);
            }
        }
    }
        
    return false;
};

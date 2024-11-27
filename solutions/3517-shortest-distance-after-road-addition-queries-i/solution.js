/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var shortestDistanceAfterQueries = function(n, queries) {
  const map = {};
  for(let i = 0; i < n - 1; i++){
      map[i] = [i + 1]
  };
    
  const answers = [];
    
  for(const q of queries){
      map[q[0]].push(q[1]);
      
      answers.push(bfs());
  }
    
    
    
  function bfs(){
      const visited = new Set();
      let steps = 0;
      const queue = [0];
      while(queue.length > 0){
          const l = queue.length;
          for(let i = 0; i < l; i++){
            const current = queue.shift();
              
            if(current === n-1){
                return steps;
            }
            if(visited.has(current)){
                continue;
            }else{
                visited.add(current);
            }

            for(const next of map[current]){
                queue.push(next);
            }
          }
          steps += 1;
      }  
    }
    return answers
};

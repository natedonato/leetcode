/**
 * @param {number[][]} routes
 * @param {number} source
 * @param {number} target
 * @return {number}
 */
var numBusesToDestination = function(routes, source, target) {
    if(source === target){
        return 0;
    }

    const stops = new Map();
    
    for(let busId = 0; busId < routes.length; busId++){
        const route = routes[busId]
        for(const stop of route){
            if(!stops.has(stop)){
                stops.set(stop, [busId])
            }else{
                stops.get(stop).push(busId);
            }
        }
    }

    const visited = new Set()
    const usedLines = new Set();

    let bus_count = 0;

    const queue = [source];
    while(queue.length > 0){
        let l = queue.length;
        
        for(let i = 0; i < l; i++){
            const current = queue.shift();
            if(current === target){
                return bus_count;
            }
            
            const lines = stops.get(current)

            if(lines){
                for(const line of lines){
                    if(!usedLines.has(line)){
                        usedLines.add(line);
                        for(const stop of routes[line]){
                            if(visited.has(stop)){
                                continue;
                            }else{
                                visited.add(stop);
                            }
                            queue.push(stop);
                        }
                    }
                }
            }
       
        }
        bus_count += 1;
    }

    return -1;
};

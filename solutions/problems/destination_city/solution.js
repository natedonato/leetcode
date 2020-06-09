/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    const graph = {};
    paths.forEach(path => {
        graph[path[0]] = path[1];
    });
    
    let currentCity = paths[0][0];
    let nextCity = graph[currentCity];
    
    while(nextCity){
        currentCity = nextCity
        nextCity = graph[currentCity]
    }
    
    return currentCity;
};
/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    let steps = 0;
    
    for(log of logs){
        if(log[0] !== '.'){
            ++steps;
        }else if(log[1] === '.' && steps > 0){
            --steps;
        }
    }
    return steps;
}
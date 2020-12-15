/**
 * @param {string[]} ops
 * @return {number}
 */
var calPoints = function(ops) {
    let scores = [];
    
    
    for(op of ops){
        if(op === '+'){
            scores.push(scores[scores.length-1] + scores[scores.length-2])
        }else if(op === 'D'){
            scores.push(2*scores[scores.length-1])
        }else if(op === 'C'){
            scores.pop();
        }else{
            scores.push(parseInt(op));
        }
    }
        
    return scores.reduce((a,e) => a + e)
};
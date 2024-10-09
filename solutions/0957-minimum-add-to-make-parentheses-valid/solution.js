/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
    let open = 0;
    let closed = 0;
    for(const char of s){
        if(char === "("){
            open += 1
        } else{
            if(open > 0){
                open -= 1;
            }else{
                closed += 1;
            }
        }
    }
    
    return open + closed;
};

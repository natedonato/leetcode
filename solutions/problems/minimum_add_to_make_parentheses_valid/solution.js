/**
 * @param {string} S
 * @return {number}
 */
var minAddToMakeValid = function(S) {
    let stack = [];
    
    
    for(const char of S){
        if(char === ')' && stack[stack.length -1] === '('){
            stack.pop();
        }else{
            stack.push(char)
        }
        
    }
    return stack.length;
};
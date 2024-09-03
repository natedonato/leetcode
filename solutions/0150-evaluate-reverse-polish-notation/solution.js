/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const stack = [];
    
    for(const item of tokens){
        if(item === "+"){
            const s2 = stack.pop();
            const s1 = stack.pop();
            stack.push(s1 + s2)
        }else if (item === "-"){
            const s2 = stack.pop();
            const s1 = stack.pop();
            stack.push(s1 - s2)
        }else if (item === "*"){
            const s2 = stack.pop();
            const s1 = stack.pop();
            stack.push(s1 * s2)
        }else if(item === "/"){
            const s2 = stack.pop();
            const s1 = stack.pop();
            stack.push(Math.trunc(s1 / s2))
        }else{
            stack.push(parseInt(item))   
        }
    }
    
    return stack.pop();
};

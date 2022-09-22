/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    
    const pair_lookup = {
        ')': '(', 
        '}': '{', 
        ']': '['    
    }
    
    for(let i = 0; i < s.length; i++){
        let current_char = s[i];
        
        if(stack.length === 0){
            stack.push(current_char)
        }else{
            if(pair_lookup[current_char] === stack[stack.length - 1]){
                stack.pop();
            }else{
                stack.push(current_char)
            }
        }
    }
    
    return (stack.length === 0);
};
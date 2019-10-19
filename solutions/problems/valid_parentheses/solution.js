/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
    const pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    };
    
    let stack = [];
    
    for(let i = 0; i < s.length; i++){
        let char = s[i];
        
        if(Object.keys(pairs).includes(char)){
            stack.push(char);   
        }else{
            let lastChar = stack.pop();
            if(pairs[lastChar] !== char){
                return false;
            }
        }
    }
    
    return(stack.length === 0);
    
};
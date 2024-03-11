/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const m = new Map([
        [")", "("],
        ["}", "{"],
        ["]", "["]
    ]);
    
    const stack = [];
    
    for(let i = 0; i < s.length; i++){
        const char = s[i];
        
        let match = m.get(char);
        
        if(match === undefined){
            stack.push(char);
        }else{
            if(stack.pop() !== match){
                return false;
            }   
        }
    }
    
    return stack.length === 0;
};


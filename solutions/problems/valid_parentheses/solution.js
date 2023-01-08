/**
 * @param {string} s
 * @return {boolean}
 */

const pairs = {
    ")":"(",
    "]":"[",
    "}":"{"
}
var isValid = function(s) {
    let stack = [];
    for(let i = 0; i < s.length; i++){
        const char = s[i];
        const pair = pairs[char];
        
        if(pair !== undefined){
            if(pair !== stack.pop()){
                return false
            }
        }else{
            stack.push(char);
        }
    }
    return stack.length === 0;
};
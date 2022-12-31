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
        console.log(char, pair);

        if(pair !== undefined){
            let last = stack.pop();
            if(last !== pair){
                return false
            }
        }else{
            stack.push(char);
        }
    }
    return stack.length === 0;
};
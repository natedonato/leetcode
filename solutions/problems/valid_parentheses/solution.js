/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    let stack = [];

    for(let i = 0; i < s.length; i++){
        char = s[i];
        if(!pairs[char]){
            stack.push(char);
        }
        else if(pairs[char] !== stack.pop()){
            return false;
        }
    }
    return stack.length === 0;
};


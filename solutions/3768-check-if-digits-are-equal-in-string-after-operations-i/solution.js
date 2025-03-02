/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function(s) {
    s = s.split("").map(el => parseInt(el));
    
    while(s.length > 2){
        first = s[0]
        next = s[1]
        for(let i = 0; i < s.length - 1; i++){
            s[i] = (first + next) % 10;
            first = s[i + 1]
            next = s[i + 2]
        }
        s.pop()
    }

    return s[0] === s[1]
};

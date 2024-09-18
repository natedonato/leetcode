/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let i = 1;
    while(s[s.length - i] === " "){
        i += 1;
    }
    
    let j = i;
    while(s[s.length - j] !== " " && s.length - j >= 0){
        j += 1;
    }
    
    return j - i;
};

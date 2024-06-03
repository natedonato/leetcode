/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var appendCharacters = function(s, t) {
    let i = 0;
    let j = 0;
    
    while(j < s.length){
        const currentCharacter = s[j];
        if(currentCharacter === t[i]){
            i += 1;
        }
        j += 1;
    };
    
    return t.length - i;    
};

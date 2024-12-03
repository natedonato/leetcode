/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    let si = 0;
    
    let output = "";
    
    for(let i = 0; i < s.length; i++){
        if(i === spaces[si]){
            output += " ";
            si++;
        }
    
        output += s[i]
    }
    
    return output;

    
    
};

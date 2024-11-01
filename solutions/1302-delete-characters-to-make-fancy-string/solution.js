/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
    let output = "";
    
    let consecutives = 0;
    let prev = "X"
    
    for(const char of s){
        if(char !== prev){
            consecutives = 1;
            prev = char;
            output += char;
        }else{
            consecutives += 1;
            if(consecutives < 3){
                output += char;
            }
        }
    }
    
    return output;
};

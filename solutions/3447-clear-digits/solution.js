/**
 * @param {string} s
 * @return {string}
 */
    const map = {
        0:true,
        1:true,
        2: true,
        3: true,
        4: true,
        5: true,
        6: true, 
        7: true,
        8: true,
        9: true
    }
    

var clearDigits = function(s) {
    const output = [];

    
    for(const char of s){
        if(map[char]){
            output.pop();
        }else{
            output.push(char)
        }
    }
    
    return output.join("");
};

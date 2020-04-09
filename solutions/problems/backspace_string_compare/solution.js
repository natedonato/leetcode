/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function(S, T) {
    
    
    var Parser = function(string) {
        let parsed = ""
        
        for(let i = 0; i < string.length; i++){
            char = string[i]
            if(char == "#"){
                if(parsed.length > 0){
                    parsed = parsed.slice(0, parsed.length-1)
                }else{
                    parsed = ""
                }
            }else{
                parsed += char
            } 
        }
        return parsed
    }
    
    return Parser(S) === Parser(T)

    
};
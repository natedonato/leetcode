/**
 * @param {string} text
 * @return {string}
 */
var entityParser = function(text) {
    const map = {
        "&quot;": "\"",
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;" : "/"
    };
    
    
    
    for(let i = 0; i < text.length; i++){
        const char = text[i]
        
        if(char === '&'){
            for(let j = i; j < i + 7; j++){
                const char2 = text[j]
                if(char2 === ";"){
                    subStr = text.slice(i, j+1);
                    let val = map[subStr]
                    if(val !== undefined){
                        text = text.replace(subStr, val);
                    }
                }
                
                
            }
        }
    }
    return text;
};
/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if(word[0] === word[0].toLowerCase()){
        for(let i = 1; i < word.length; i++){
            if(word[i] !== word[i].toLowerCase()){
                return false
            }
        }
        return true
    }else{
        if(word.length < 2){
            return true
        }        
        if(word[1] === word[1].toLowerCase()){
           for(let i = 2; i < word.length; i++){
                if(word[i] !== word[i].toLowerCase()){
                    return false
                }
            }
            return true;
        }else{
            for(let i = 1; i < word.length; i++){
                if(word[i] !== word[i].toUpperCase()){
                    return false
                }
            }
            return true
        }
    }
};
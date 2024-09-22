/**
 * @param {string[]} message
 * @param {string[]} bannedWords
 * @return {boolean}
 */
var reportSpam = function(message, bannedWords) {
    let count = 0;
    let s = new Set(bannedWords);
    
    for(const word of message){
        if(s.has(word)){
            count += 1;
            if(count >= 2){
                return true;
            }
        }
    }
    
    return false;
};

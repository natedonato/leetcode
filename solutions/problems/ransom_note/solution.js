/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    for(const char of ransomNote){
        if(magazine.indexOf(char) === -1){
            return false
        }
        magazine = magazine.replace(char, '');
    }
    return true
};
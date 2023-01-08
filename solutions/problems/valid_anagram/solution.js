/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let count = {}
    if(s.length !== t.length){
        return false;
    }
    for(const char of s){
        count[char] = (count[char] || 0) + 1
    }
    for(const char of t){
        if(count[char]){count[char] -= 1}
        else{
            return false
        }
    }
    return true;
};
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let seen = [];
    let max = 0;

    for(const char of s){
        let idx = seen.indexOf(char);

        if(idx !== -1){
            seen = seen.slice(idx + 1)
        }
        
        seen.push(char);
        max = Math.max(seen.length, max);
    }
    
    return max
};
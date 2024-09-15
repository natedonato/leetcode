/**
 * @param {string} s
 * @return {number}
 */
var findTheLongestSubstring = function(s) {
    const seen = {};
    let max = 0;
    seen["00000"] = -1;
    current = [0,0,0,0,0];
    
    for(let i = 0; i < s.length; i++){
        const char = s[i]
        const idx = "aeiou".indexOf(char);
        if(idx > -1){
            current[idx] = current[idx] === 1 ? 0 : 1;
        }
        currentKey = current.join("");
        if(seen[currentKey] !== undefined){
            length = i - seen[currentKey];
            max = Math.max(max, length);
        }else{
            seen[currentKey] = i;
        }
    }
    
    return max;
};

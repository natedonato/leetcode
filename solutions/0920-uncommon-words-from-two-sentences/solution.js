/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    const count = {}
    s1 = s1 + " " + s2
    for(const word of s1.split(" ")){
        !count[word] && (count[word] = 0)
        count[word] += 1
    }
    
    const output = []
    
    for(const [key, val] of Object.entries(count))
        {
            if(val === 1){output.push(key)}
        }
    return output
};

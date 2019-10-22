/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    let count = {};
    
    s.split("").forEach(char =>{
        if(!count[char]){
            count[char] = 1
        }else{
            count[char] += 1
        }
    })
    
    let sorted = Object.keys(count).sort((a,b) => count[b] - count[a]);
    
    let output = "";
    sorted.forEach(char =>{
        output += char.repeat(count[char]);
    });
    
    return output
};
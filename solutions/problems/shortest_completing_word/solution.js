/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
var shortestCompletingWord = function(licensePlate, words) {
    count = {}
    
    licensePlate.split('').forEach(char => {
        code = char.charCodeAt(0)
        if((code >= 97 && code <= 122) || (code >= 65 && code <= 90 )){
            count[char.toLowerCase()] ? count[char.toLowerCase()] += 1 : count[char.toLowerCase()] = 1
        }
    }
    )
    
    console.log(Object.keys(count))

    let min = "123456789012345678901234567"
    for(let word of words){
    if(word.length < min.length){
        let subcount = {...count}
        for(let i = 0; i < word.length; i++){
            char = word[i]
            if(subcount[char]){
                subcount[char] -= 1;
            }
            
        }
        if(Object.keys(subcount).filter(el => subcount[el] > 0).length == 0){
            min = word
        }
    }
    }
    return min
};
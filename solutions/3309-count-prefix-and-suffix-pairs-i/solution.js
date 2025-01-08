/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) {
    let count = 0
    for(let i = 0; i < words.length - 1; i++){
        for(let j = i + 1; j < words.length; j++){
            let w1 = words[i];
            let w2 = words[j];
            if(presuf(w1,w2)){
                ++count
            }
        }
    }

    return count
}


function presuf(w1, w2){
    if(w2.length < w1.length){
        return false
    }
    return (w1 === w2.slice(0,w1.length) && w1 === w2.slice(w2.length - w1.length));

}

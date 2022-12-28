/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    
    let output = [];
    let seenInAll = {};

    // count chars in initial word;
    for(let i = 0; i < words[0].length; i++){
        const char = words[0].charAt(i);
        if(!seenInAll[char]){
            seenInAll[char] = 1;
        }else{
            seenInAll[char] += 1;
        }
    }
    
    // loop through all words
    for(let i = 1; i < words.length; i++){
        
        // count chars in current word (only for chars already in our collection)
        const seenInWord = {};
        const word = words[i];
        for(let i = 0; i < word.length; i++){
            const char = word[i];
            if(seenInAll[char]){
                if(seenInWord[char] === undefined){
                    seenInWord[char] = 1;
                }else{
                    seenInWord[char] += 1;
                }
            }
        }
        
        // filter out characters that aren't seen in current word or seen less than before
        for(const[key, val] of Object.entries(seenInAll)){
            if(seenInWord[key] === undefined){
                delete seenInAll[key];
            }else{
                seenInAll[key] = Math.min(seenInWord[key], val)
            }
        }
    }
    
    // rejoin seen characters into array
    for(const [key,val] of Object.entries(seenInAll)){
        for(let i = 0; i < val; i++){
            output.push(key);
        }
    }
    
    return output;
};
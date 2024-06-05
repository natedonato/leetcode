/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    let collection = new Map();
    
    for(let i = 0; i < words[0].length; i++){
        if(!collection.get(words[0][i])){
            collection.set(words[0][i],1)
        }else{
            collection.set(words[0][i], collection.get(words[0][i]) + 1);
        }
    }
    
    for(let j = 1; j < words.length; j++){
        let new_collection = new Map();
        const word = words[j];
        for(let i = 0; i < word.length; i++){
            const char = word[i];
            
            if(collection.has(char) && collection.get(char) > (new_collection.get(char) ?? 0)){
                new_collection.set(char, (new_collection.get(char) ?? 0) + 1);
            }
            
        }
    
        collection = new_collection;
    }

    const arr = [];

    collection.forEach((key, val) => {
            for(let i = 0; i < key; i++){
            arr.push(val);
        }
    });

    return arr;
};

/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */



var replaceWords = function(dictionary, sentence) {    
    const trie = {
        children: {}
    }
    
    for(const word of dictionary){
        add_to_trie(word, trie);
    }
    
    sentence = sentence.split(" ").map(el => check_the_trie(el, trie));

    return sentence.join(" ");
};

function check_the_trie(word, trie){
    let current_node = trie;
    
    for(let i = 0; i < word.length; i++){
        const next_char = word[i];
        if(current_node.children[next_char] == undefined){
            return word;
        }else{
            current_node = current_node.children[next_char];
            
            if(current_node.is_word){
                return current_node.word;
            }
        }
    }
    
    return word;
}


function add_to_trie(word, trie){
    
    let current = trie;
    
    for(let i = 0; i < word.length; i++){
        const next_char = word[i];
                
        if(current.children[next_char] == undefined){
            
            current.children[next_char] = {
                children: {}
            }
        }
        
        current = current.children[next_char]
    }
    
    current.is_word = true;
    current.word = word;
}

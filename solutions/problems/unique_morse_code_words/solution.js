/**
 * @param {string[]} words
 * @return {number}
 */

const morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];

const alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

var uniqueMorseRepresentations = function(words) {
    let set = new Set();
    
    for(const word of words){
        let str = ""
        for(let i = 0; i < word.length; i++){
            let char = word.charAt(i);
            
            let code = morse[alph.indexOf(char)];
            str = str + code;
        }
        set.add(str);
    }
    
    
    return set.size;
};
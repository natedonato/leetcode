/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    let reversed = ''
    let i = 0;
    let reversing = true;
    while(reversing){
        if(i >= word.length){
            return word;
        }
        
        const nextChar = word.charAt(i);
        reversed = nextChar + reversed 
        if(nextChar === ch){
            return reversed + word.slice(i + 1);   
        }
        i++
    }
};

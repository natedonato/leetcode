/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let character_array = s.split('');

    
    // test if character is vowel
    function isVowel(char){
        return 'aeiouAEIOU'.includes(char) === true;
    };
    
    // arrays to collect seen vowels and the indexes we have seen them at
    let vowels = [];
    let vowel_indices = [];
        
    // go through each character of string, check if it's a vowel
    for(let i = 0; i < character_array.length; i++){
        let current_char = character_array[i];
        
        // if it is a vowel, record the character and the index of the vowel
        if(isVowel(current_char)){
           vowels.push(current_char);
            // add indices to index collection in reverse order by unshift
           vowel_indices.unshift(i);
         }        
    }
    
    // use our two collections to assign seen vowels to their seen indexes (indexes are reversed, so vowels will be reversed)  
    for(let i = 0; i < vowels.length; i++){
        let idx = vowel_indices[i];
        let char = vowels[i];
        character_array[idx] = char;
    }
    
    // rejoin edited array into string and return
    return character_array.join('')
};
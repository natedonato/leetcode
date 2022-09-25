/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    s = s.split('');
    
    let left = 0
    let right = s.length - 1;
    let dict = {
        "a": true,
        "e": true,
        "i": true,
        "o": true,
        "u": true,
        "A": true,
        "E": true,
        "I": true,
        "O": true,
        "U": true
    };
    
    function isVowel(char){
        return (dict[char] === true) 
    };
    
    
    while(left < right){
       while(!isVowel(s[left]) && !(left >= s.length -1)){
            left += 1;
        };
        while(!isVowel(s[right]) && !(right <= 0)){
            right -= 1;
        };

        if(left < right){
            let temp = s[left];
            s[left] = s[right];
            s[right] = temp;
        };

        left += 1;
        right -= 1;
    }
    
    return s.join('')
};
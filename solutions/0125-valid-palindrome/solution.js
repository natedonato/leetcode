/**
 * @param {string} s
 * @return {boolean}
 */
const CHAR_ZERO = "0".charCodeAt(0);
const CHAR_NINE = "9".charCodeAt(0);
const CHAR_A_LOWER = "a".charCodeAt(0);
const CHAR_Z_LOWER = "z".charCodeAt(0);
const CHAR_A_UPPER = "A".charCodeAt(0);
const CHAR_Z_UPPER = "Z".charCodeAt(0);

var isPalindrome = function(s) {
    let left = 0;
    let right = s.length - 1;
    
    while(left < right){
        while(!isAlphaNumeric(s[left])){
            left += 1;
            if(left >= right){
                return true
            }
        }
        
        while(!isAlphaNumeric(s[right])){
            right -= 1;
        };
                
        if(s[left].toLowerCase() !== s[right].toLowerCase()){
            return false;
        }
        left += 1;
        right -= 1;
    }
    
    return true;
};

// (character) =>
// returns true if a character is lower case alpha or numeric
var isAlphaNumeric = function(c){
    let code = c.charCodeAt(0);
    if((CHAR_ZERO <= code && CHAR_NINE >= code)
       || (CHAR_A_LOWER <= code && CHAR_Z_LOWER >= code)
       || (CHAR_A_UPPER <= code && CHAR_Z_UPPER >= code)
    ){
        return true;
    }
    
    return false;
};

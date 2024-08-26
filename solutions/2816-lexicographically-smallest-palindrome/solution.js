/**
 * @param {string} s
 * @return {string}
 */
var makeSmallestPalindrome = function(s) {
    s = s.split("");
    
    let i = 0;
    let j = s.length - 1;
    
    while(i < j){
        if(s[i] > s[j]){
            s[i] = s[j]
        }else if(s[j] > s[i]){
            s[j] = s[i]
        }
        
        i++;
        j--;
    }
    
    return s.join("");
};

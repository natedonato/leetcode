/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if(s.length === 1){
        return s[0];
    };
    
    let max = s[0];
    
    for(let i = 0; i < s.length - 1; i++){
        expand(i,i);
        expand(i, i + 1);
        
    }
    
    function expand(i,j){
        let current = "";
        while(i >= 0 && j < s.length ){
            if(i === j){
                current += s[i];
                i -= 1;
                j += 1;
            }else{
                if(s[i] !== s[j]){
                    break;
                }else{
                    current = s[i] + current + s[j];
                    i -= 1;
                    j += 1;
                }
            }
        }
        if(current.length > max.length){
            max = current;
        }
    }
    
    return max;
};

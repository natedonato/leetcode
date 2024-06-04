/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    const counts = new Map();
    
    for(let i = 0; i < s.length; i++){
        if(!counts.get(s[i])){
            counts.set(s[i], 1);
        }else{
            counts.set(s[i], counts.get(s[i]) + 1);
        }
    }
    
    let odd = false;
    let length = 0;
    
    counts.forEach((val, key) => {
        if(val % 2 !== 0){
            odd = true;
        }
        
        length += Math.floor(val / 2);
        
    })
    
    length *= 2;
    if(odd){
        length += 1
    }

    return length;
};


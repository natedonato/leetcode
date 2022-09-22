/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    // return false immediately if strings aren't same length
    if(s.length !== t.length){
        return false;
    }
    
    // set up a dictionary to track equivalent characters
    let dict = {};
    let reverse_dict = {};
    
    
    // iterate through characters of both strings at the same pace
    for(let i = 0; i < s.length; i++){
        const charA = s.charAt(i);
        const charB = t.charAt(i);
    
        if(dict[charA] === undefined){
            if(reverse_dict[charB] !== undefined){
                return false
            }else{
                dict[charA] = charB;
                reverse_dict[charB] = charA;
            }
        }else{
            if(dict[charA] !== charB){
                return false;
            }
        }
    }
    
    return true;
};
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const count = new Map();
    const count2 = new Map();
    
    for(let i = 0; i < s.length; i++){
        if(count.get(s.charAt(i)) === undefined){
            count.set(s.charAt(i), 0)
        }
        count.set(s.charAt(i), count.get(s.charAt(i)) + 1)
    }
    
      for(let i = 0; i < t.length; i++){
        if(count2.get(t.charAt(i)) === undefined){
            count2.set(t.charAt(i), 0)
        }
        count2.set(t.charAt(i), count2.get(t.charAt(i)) + 1)
    }
    
    if(count.size !== count2.size){
        return false
    }
    for(const [key, val] of count.entries()){
        if(count2.get(key) !== val){
            return false
        }   
    }
    return true;
};

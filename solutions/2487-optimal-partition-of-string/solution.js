/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function(s) {
    let count = 1;
    let set = new Set();
    
    for(const c of s){
        if(!set.has(c)){
            set.add(c)
        }else{
            set.clear();
            set.add(c);
            count += 1;
        }
    }
    
    return count;
};

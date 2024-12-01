/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
    const set = new Set();
    
    for(const item of arr){
        if(set.has(item * 2) || set.has(item / 2)){
            return true;
        }else{
            set.add(item);
        }
    }
    
    return false;
};

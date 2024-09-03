/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const s = new Set();
    
    while(true){
        if(n === 1){
            return true;
        }else if(s.has(n)){
            return false;
        }else{
            s.add(n);
            let sum = 0;
            n.toString().split("").forEach(el => sum += parseInt(el)**2);
            n = sum;
        }    
    }
    
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @return {boolean}
 */
var canArrange = function(arr, k) {
    const remainders = {};
    
    for(const el of arr){
        const r = ((el % k) + k) % k;
        remainders[r] = (remainders[r] || 0) + 1;
    }
        
    for(let r of Object.keys(remainders)){
        r = parseInt(r);
        // console.log("r", r);
        if(r !== 0){
            const compliment = k - r;
            const count = remainders[r];
            if(compliment === r){                
                if(count % 2 !== 0){
                    return false;
                }
            }else{
                if(remainders[compliment] !== count){
                    return false;
                }
            }
        }
    }
    
    return true;    
};

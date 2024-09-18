/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function(n) {
    let gap = 0;
    let max = 0;
    n = n.toString(2);
    
    for(let i = 0; i < n.length; i++){        
        const bit = n[i];
        if(bit === "1"){
            if(gap > max){
                max = gap;
            }
            gap = 1;
        }else{
            gap += 1;
        }
    }
    
    
    return max;
};

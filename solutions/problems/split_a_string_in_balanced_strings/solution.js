/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    
    let balancedCount = 0;
    let lCount = 0;
    let rCount = 0;
    let i = 0;
    
    
    while(i < s.length){
        let nextChar = s.charAt(i);
        
        if(nextChar === 'L'){
            lCount += 1;
        }else if(nextChar === 'R'){
            rCount += 1;
        }
        
        if(lCount !== 0 && lCount === rCount){
            balancedCount += 1;
            lCount = 0;
            rCount = 0;
        }    
        
        i += 1;
    }
    
    return balancedCount;
};
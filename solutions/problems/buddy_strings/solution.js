/**
 * @param {string} A
 * @param {string} B
 * @return {boolean}
 */
var buddyStrings = function(A, B) {
    if(A.length !== B.length){return false};
    
    
    let counts = {};
    let dups = false;
    
    if(A === B){  
        A.split("").forEach(char => {
            if(!counts[char]){counts[char] = 1; console.log(counts)}
        else{
            dups = true
        }
        });
        return dups; 
    }
    
    let count = 0; 
    let cached = []; 


    for(let i = 0; i < A.length; i++){
        
        if(A[i] !== B[i]){
            count++;
            
            if(count === 1){
                cached = [A[i],B[i]]
            }else if(count === 2)
                if(A[i] !== cached[1] || B[i] !== cached[0]){   
                   
                    return false
                }
            if(count > 2)
            {
                return false; 
        }        
    }}
    
    if(count === 0) {return false;} 
    return true;
};
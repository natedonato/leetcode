/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let bounds = [-(2**31), 2**31 -1]
    
    let i = 0;
    let ints = '1234567890'
    let scalar = 1
    let output = 0;
    
    while(s[i] === " "){
        i += 1
    };
    
    if(s[i] === '+'){
        i++;
    }else if(s[i] === '-'){
        scalar = -1;
        i++;
    }
    
    if(!ints.includes(s[i])){
        return 0;
    }else{
        while(ints.includes(s[i])){
            output = output * 10 + parseInt(s[i]);  
            i++;
        }
        output *= scalar;
        
        if(output > bounds[1]){
            output = bounds[1]
        }else if(output < bounds[0]){
            output = bounds[0]
        }
        
    }
    
    
    return output;
};
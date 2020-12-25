/**
 * @param {string} S
 * @return {number[]}
 */
var diStringMatch = function(S) {
    let max = S.length;
    let min = 0;
    let output = [];
    
    for(const char of S){
        if(char === "I"){
            output.push(min)
            ++min;
        }else{
            output.push(max)
            --max;
        }
    }
    
    while(min <= max){
        output.push(min);
        ++min;
    }
    
    return output;
};
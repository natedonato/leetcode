/**
 * @param {string} S
 * @param {character} C
 * @return {number[]}
 */
var shortestToChar = function(S, C) {
    let last;
    let output = [];
    for(let i = 0; i < S.length; i++){
        if(S[i] === C){
            if(last === undefined){
                let current = i;
                for(let j = 0; j <= i; j++){
                    output[j] = current;
                    current -= 1;
                }    
                last = i;
            }else{
                let length = i - last + 1;
                let max = (length - 1) / 2;
                let next = []
                if(max === Math.floor(max)){
                    next.push(max);
                    max -= 1;
                }else{
                    max = Math.floor(max);
                }
                
                while (max >= 0){
                    next.push(max)
                    next.unshift(max)
                    max -= 1;
                }
                output.push(...next.slice(1));                
                last = i;
            }
        }
    }
    
    let count = 1
    for(let i = last + 1; i < S.length; i++){
        output.push(count);
        count += 1;
    }
    return output;
};
/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    let output = [];
    loop1:
    for(let i = left; i <= right; i++){
        let digits = Array.from(String(i), Number);
        
        for(const digit of digits){
            if(digit === 0 || i % digit !== 0){
                continue loop1;
            }
        }
        output.push(i);
    }
    return output;
};
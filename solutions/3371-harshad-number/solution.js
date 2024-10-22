/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
    const y = x;
    let sum = 0;
    
    while(x > 0){
        sum += x % 10;
        x = Math.floor(x/10);
    }
    
    if(y % sum === 0){
        return sum
    }else{
        return -1;
    }
};

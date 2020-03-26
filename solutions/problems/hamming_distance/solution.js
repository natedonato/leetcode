/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    let count = 0;
    x = toBinaryArray(x);
    y = toBinaryArray(y);
    
    for(let i = 0; i < x.length; i++){
        if(x[i] !== y[i])
            count += 1
    }
    
    return count;
};


var toBinaryArray = function(num){
    bStr = ''
    
    while(num > 0){
        if(num % 2 === 0){
        bStr += '0'
        }else{bStr += 1}
        num = Math.floor(num / 2)
    }
    
    while(bStr.length < 32){
        bStr += '0'
    }
    
    return bStr.split('').reverse()
    
}
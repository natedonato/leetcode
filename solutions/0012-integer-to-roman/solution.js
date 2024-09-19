/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let output = "";
    output = makeDigit(num % 10, "I","V","X");
    output = makeDigit(Math.floor(num / 10) % 10, "X","L","C") + output;
    output = makeDigit(Math.floor(num / 100) % 10, "C","D","M") + output;
    output = makeDigit(Math.floor(num / 1000) % 10, "M","N/A","N/A") + output;
    
    
    return output;
};


function makeDigit(digit, one, five, ten){
    let output = ""
    if(digit === 9){
        output += one + ten;
        return output;
    }else if(digit >= 5){
        output += five;
        for(let i = 0; i < digit - 5; i++){
            output += one;
        }
        return output;
    }else if(digit === 4){
        output += one;
        output += five;
        return output;
    }else{
        for(let i = 0; i < digit; i++){
            output += one;
        }
        return output;
    }
}

/**
 * @param {string} expression
 * @return {number[]}
 */
const memo = {};

var diffWaysToCompute = function(expression) {
    if(expression.length <= 2){
        return [parseInt(expression)];
    }

    const output = [];
    const operators = "+-*"
    
    for(let i = 0; i < expression.length; i++){
        const char = expression[i]
        if(operators.includes(char)){
            const leftResults = diffWaysToCompute(expression.slice(0,i));
            const rightResults = diffWaysToCompute(expression.slice(i+1));
            for(const leftResult of leftResults){
                for(const rightResult of rightResults){
                    output.push(doMath(leftResult, char, rightResult))
                }
            }
            
        }
    }
    
    memo[expression] = output;
    
    return output;
};

function doMath(a, operator, b){
    if(operator === "+"){
        return a + b
    }else if(operator === "-"){
        return a - b
    }else if(operator === "*"){
        return a * b
    }else{
        throw new Error('unrecognized operator')
    };
}

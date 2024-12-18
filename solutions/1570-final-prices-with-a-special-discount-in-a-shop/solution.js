/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    const stack = [];
    
    for(let i = 0; i < prices.length; i++){
        const price = prices[i];
        
        while(stack.length > 0 && price <= stack[stack.length - 1][0]){
            let old = stack.pop();
            
            prices[old[1]] = prices[old[1]] - price;
        }
        
        stack.push([price, i])    
    }
    
    return prices;
};

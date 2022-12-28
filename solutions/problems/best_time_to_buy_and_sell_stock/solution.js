/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let lowestPrice = prices[0];
    let maxProfit = 0;
    
    for(const currentPrice of prices){
        let potentialGain = currentPrice - lowestPrice;
        
        if(potentialGain > maxProfit){
            maxProfit = potentialGain;
        }
        
        if(lowestPrice > currentPrice){
            lowestPrice = currentPrice;
        }
        
    }    
    return maxProfit;
};
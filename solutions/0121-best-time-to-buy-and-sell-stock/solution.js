/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let i = 0;
    let currentMin = prices[0];
    let maxProfit = 0;
    
    for(let i = 1; i < prices.length; i++){
        let profit = prices[i] - currentMin;
        if(profit > maxProfit){
            maxProfit = profit;
        }
        if(currentMin > prices[i]){
            currentMin = prices[i]
        }   
    }
    
    return maxProfit
};

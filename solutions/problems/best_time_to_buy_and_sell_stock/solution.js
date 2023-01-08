/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = prices[0];
    let maxProfit = 0;

    for(const price of prices){
        if(price - minPrice > maxProfit){
            maxProfit = price - minPrice;
        }
        if(minPrice > price){
            minPrice = price;
        }
    }

    return maxProfit
};
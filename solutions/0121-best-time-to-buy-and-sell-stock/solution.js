/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let currentMin = prices[0];
    let currentMax = 0;

    for(let i = 1; i < prices.length; i++){
        const currentP = prices[i];
        if((currentP - currentMin) > currentMax){
            currentMax = currentP - currentMin
        }

        if(currentP < currentMin){
            currentMin = currentP
        }

    }
    return currentMax;
};

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let local_low = null
    let local_high = null
    let total_profit = 0

    for(const price of prices){    
        
        if(local_high === null || local_low === null){
            local_high = local_low = price
        }
        
        if(price < local_low){
            total_profit += local_high - local_low
            local_low = local_high = price
        }
        else if(price > local_high){
            local_high = price
        }
        else if(price < local_high){
            total_profit += local_high - local_low
            local_high = local_low = price
        }
        
    } 
 
    total_profit += local_high - local_low
 
    return total_profit
};
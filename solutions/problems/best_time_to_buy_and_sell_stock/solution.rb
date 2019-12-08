# @param {Integer[]} prices
# @return {Integer}
    
def max_profit(prices)
    minprice = prices[0]
    maxprofit = 0;

    prices.each_with_index do |price, idx|
        if(price < minprice)
            minprice = price
        else
        profit = price - minprice
        if(profit > maxprofit)
            maxprofit = profit
        end
        end
    
    
    end  
    
    return maxprofit
end
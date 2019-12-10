/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

//  amount
//  1 + (amount - coin value)
//  
//
//
//
//
//
//
var coinChange = function(coins, amount, memo = {}) {
    if(amount < 0){return -1}
    if(amount === 0){return 0}
    if(memo[amount]){return memo[amount]}

    let best = Infinity;
    
    coins.forEach(coin =>{
        let newAmount = amount - coin;
        let num_coins = coinChange(coins, newAmount, memo)
        if(num_coins !== -1){
            if(best > num_coins + 1){best = num_coins + 1}
        }
    })
    memo[amount] = best
    if(best === Infinity){memo[amount] = -1; return -1}
    return best 
};
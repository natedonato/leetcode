var change = function(amount, coins) {
    const memo = {};
    coins = coins.sort((a,b) => b - a);
    return change(amount, coins);
    
    function change(amount, coins){
        if(amount === 0){
            return 1;
        }else if(amount < 0){
            return 0;
        };
        
        if(memo[coins[0]+":"+amount] !== undefined){
            return memo[coins[0]+":"+amount];
        }

        
        let total = 0;
        
       for(let i = 0; i < coins.length; i++){
           total += change(amount - coins[i], coins.slice(i))
       } 

        memo[coins[0]+":"+amount] = total;
        
        return total
    };
};

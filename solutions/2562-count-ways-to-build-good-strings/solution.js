/**
 * @param {number} low
 * @param {number} high
 * @param {number} zero
 * @param {number} one
 * @return {number}
 */
var countGoodStrings = function(low, high, zero, one) {
    const memo = new Map();

    return dfs(0);

    function dfs(currentLength){
        if(memo.has(currentLength)){
            return memo.get(currentLength)
        }
    
        if(currentLength > high){
            return 0;
        }

        let ans = 0;

        if(low <= currentLength){
            ans += 1;
        };
    
        ans += dfs(currentLength + zero)

        ans += dfs(currentLength + one)
    
        memo.set(currentLength, ans);
        ans %= ((10 ** 9) + 7)  
        
        return ans;
    }


};

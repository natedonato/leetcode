/**
 * @param {number[]} chalk
 * @param {number} k
 * @return {number}
 */
var chalkReplacer = function(chalk, k) {
    const sum = chalk.reduce((a,e) => a+e, 0)
    
    k %= sum;
    
    for(let i = 0; i < chalk.length; i++){
        if(chalk[i] > k){
            return i;
        }else{
            k -= chalk[i]
        }
    }
};

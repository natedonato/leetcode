/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    happiness = happiness.sort((a,b) => b - a);
    
    let total = 0;
    for(let i = 0; i < k; i++){
        const value = happiness[i] - i;
        if(value > 0){
            total += value
        }
    }
    
    return total;
};

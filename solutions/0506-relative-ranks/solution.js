/**
 * @param {number[]} score
 * @return {string[]}
 */
var findRelativeRanks = function(score) {
    const sorted = score.toSorted((a,b) => b-a);
    
    const ranks = {};
    for(let i = 0; i < sorted.length; i++){
        if(i === 0){
            ranks[sorted[i]] = "Gold Medal"
        }else if(i === 1){
            ranks[sorted[i]] = "Silver Medal"
        }else if(i === 2){
            ranks[sorted[i]] = "Bronze Medal"
        }else{
            ranks[sorted[i]] = String(i + 1)
        }
    }
    
    score = score.map(el => {
        return ranks[el]
    });
    
    
    return score;
};

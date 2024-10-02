var arrayRankTransform = function(arr) {
    const sortedArr = arr.toSorted((a,b) => a - b);
    
    // k: array value, v: rank
    const ranks = new Map();
    let rank = 0;
    
    for(let i = 0; i < sortedArr.length; i++){
        if(sortedArr[i] !== sortedArr[i - 1]){
            rank += 1;
            ranks.set(sortedArr[i], rank);
        }
    }
    
    return arr.map(el => ranks.get(el));
};

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    stones = stones.sort((a,b)=> a-b)

    while(stones.length > 1){
        let a = stones.pop()
        let b = stones.pop()
        if(a !== b){stones.push(Math.abs(a - b)); stones = stones.sort((a,b)=> a-b)}
    }
    
    return stones
    
    
};
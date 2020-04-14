/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    
    //initial sort 
    stones = stones.sort((a,b)=> a-b)

    //if there is more than one stone in the pile we must smash the two heaviest
    while(stones.length > 1){
        
        //since array is sorted pop not only gets the heaviest but also removes it from the array, so we do this twice
        let a = stones.pop()
        let b = stones.pop()
        
        //if they are equal weight there is nothing left to do, since they are both crushed and nothing is left over
        
        //if they are not equal we must add the remaining stone to the pile.  we do another sort operation when we add to make sure it is in the right place.  an improvement would be to use a heap
        if(a !== b){stones.push(Math.abs(a - b)); stones = stones.sort((a,b)=> a-b)}
    }
    
    return stones
    
    
};
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    
    const output = [];
    
    function btrack(prev, numOpen, numClosed){
        if(numOpen === n && numClosed === n){
            output.push(prev);
            return;
        }
        
        if(numOpen < n){
            btrack(prev + "(", numOpen + 1, numClosed);
        }
        
        if(numClosed < numOpen){
            btrack(prev + ")", numOpen, numClosed + 1)
        }
    }
    btrack("", 0,0);
    
    return output;
};

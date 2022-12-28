/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    let solutions = 0;

    function solveRecurse(boardState, n){
        if(boardState.length === n){
            solutions += 1;
            return;
        }

        for(let i = 0; i < n; i++){
            if(!boardState.some((el, idx) => {
                return (el === i || el + (boardState.length - idx) === i || el - (boardState.length - idx) === i)
            })){
                boardState.push(i);
                solveRecurse(boardState,n)
                boardState.pop();
            }
        }
    }

    solveRecurse([],n,0);
    return solutions;
};
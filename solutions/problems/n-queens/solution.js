/**
 * @param {number} n
 * @return {string[][]}
 */
var serializeBoard = function(boardState, n){
    let board = [];

    for(let i = 0; i < boardState.length; i++){
        let row = '';
        for(let j = 0; j < n; j++){
            if(boardState[i] === j){
                row += "Q";
            }else{
                row += '.';
            }
        }
        board.push(row);
    }
    return board;
}

var solveNQueens = function(n) {
    const solutions = [];

    function solveRecurse(boardState, n){
        if(boardState.length === n){
            solutions.push(serializeBoard(boardState, n));
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
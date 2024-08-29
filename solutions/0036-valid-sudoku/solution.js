/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    // rows
    for(let i = 0; i < board.length; i++){
        const set = board[i];
        if(!validSet(set)){
            return false;
        }
    }
    
    // cols
    for(let j = 0; j < board.length; j++){
        const set = [];
        for(let i = 0; i < board.length; i++){
            set.push(board[i][j])
        }
        if(!validSet(set)){
            return false;
        }
    }
    
    // 3x3 boxes
    for(let iOff = 0; iOff < 3; iOff++){
        for(let jOff = 0; jOff < 3; jOff++){
            const set = [];
            for(let i = 0; i < 3; i++){
                for(let j = 0; j < 3; j++){
                    set.push(board[i + 3 * iOff][j + 3 * jOff])
                }
            }
            if(!validSet(set)){
                return false;
            }
        }
    }
        
    
    return true;
};

function validSet(set){
    const count = {};
    
    for(const item of set){
        if(item !== "."){
            if(count[item]){
                return false;
            }else{
                count[item] = 1;
            }
        }
    }
    return true;
}

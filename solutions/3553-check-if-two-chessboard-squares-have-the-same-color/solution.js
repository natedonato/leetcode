/**
 * @param {string} coordinate1
 * @param {string} coordinate2
 * @return {boolean}
 */
var checkTwoChessboards = function(coordinate1, coordinate2) {
    const cols = 'abcdefgh';
    
    return getColor(coordinate1) === getColor(coordinate2);
    
    function getColor(coord){
        const col = cols.indexOf(coord[0]);
        if(col % 2 === 0){
            return parseInt(coord[1]) % 2 === 1;
        }else{
            return parseInt(coord[1]) % 2 === 0;
        }
    }
};

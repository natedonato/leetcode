/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const object = findZeroes(matrix);
    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            if(object.rows[i] || object.columns[j])
                matrix[i][j] = 0
        }
    }
    
    return matrix;
};

var findZeroes = function(matrix){
    rows = {};
    columns = {};
    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            if(matrix[i][j] === 0){
                rows[i] = true;
                columns[j] = true;
            }        
        }
    } 
    return({rows, columns});
    
}
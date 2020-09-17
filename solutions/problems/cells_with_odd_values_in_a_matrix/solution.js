/**
 * @param {number} n
 * @param {number} m
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function(n, m, indices) {
    let arr = new Array(n).fill(null).map(() => (new Array(m).fill(0)));
    
    for(const tup of indices){
        IncrementRow(tup[0]);
        IncrementCol(tup[1]);
    }
    
    
    function IncrementRow(row){
        for(let i = 0; i < m; i++){
            arr[row][i] += 1;
        }
    }
    
    function IncrementCol(col){
        for(let i = 0; i < n; i++){
            arr[i][col] += 1;
        }
    }
    
    let count = 0;
    
    for(const row of arr){
        for(const el of row){
            console.log(el)
            if(el % 2 !== 0){
                count += 1;
            }
        }
    }
    
    return count;
};
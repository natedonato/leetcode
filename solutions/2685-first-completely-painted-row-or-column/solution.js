/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
var firstCompleteIndex = function(arr, mat) {
    const memo = {}

    for(let i = 0; i < mat.length; i++){
        for(let j = 0; j < mat[0].length; j++){
            const el = mat[i][j]
            memo[el] = [i,j]
        }
    }

    const rows = new Array(mat.length).fill(0)
    const cols = new Array(mat[0].length).fill(0)

    for(let i = 0; i < arr.length; i++){
        const idx = arr[i];
        const [r,c] = memo[idx];

        rows[r] += 1
        cols[c] += 1

        if(rows[r] === mat[0].length || cols[c] === mat.length){
            return i
        }


    }
};

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    const output = [];
    for(let i = 0; i < arr.length; i+= size){
        const row = [];
        for(let j = 0; j < size && i+j < arr.length; j++){
            row.push(arr[i + j])
        }
        output.push(row);
    }
    return output;
};
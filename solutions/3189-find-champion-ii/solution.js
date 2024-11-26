/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findChampion = function(n, edges) {
    const arr = new Array(n).fill(0);
    for(const e of edges){
        console.log(e);
        arr[e[1]] += 1;
    }
    console.log(arr);
    let output = -1;
    
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === 0){
            if(output === -1){
                output = i   
            }else{
                return -1;
            }
        }
    }
    
    return output;
};

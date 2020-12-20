/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    let count = 0;
    for(let i = 0; i < arr.length-2; i++){
        for(let j = i+1; j < arr.length - 1; j++){
            for(let k = j + 1; k < arr.length; k++){
                let [_a, _b, _c] = [arr[i]-arr[j], arr[j]-arr[k], arr[i]-arr[k]].map(el => Math.abs(el));
                if(_a <= a && _b <= b && _c <= c){
                    count++;
                }
                
            }
        }
    }
    return count;
};
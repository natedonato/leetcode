/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const out = []

    for(let i = 0; i < arr.length; i++){
        out.push(fn(arr[i], i))
    }

    return out;
};

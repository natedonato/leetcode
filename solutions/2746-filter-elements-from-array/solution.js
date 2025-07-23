/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const out = []

    for(let i = 0; i < arr.length; i++){
        el = arr[i]
        if(fn(el, i)){
            out.push(el)
        }
    }

    return out;
};

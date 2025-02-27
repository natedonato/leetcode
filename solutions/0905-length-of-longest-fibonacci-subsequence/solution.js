/**
 * @param {number[]} arr
 * @return {number}
 */
var lenLongestFibSubseq = function(arr) {
    const nums = new Set(arr);
    let max = 0;

    for(let i = 0; i < arr.length - 1; i++){
        for(let j = i+1; j < arr.length; j++){
            let len = 2;
            let n1 = arr[i];
            let n2 = arr[j];
            let next = n1 + n2
            while(nums.has(next)){
                len += 1;
                n1 = n2;
                n2 = next;
                next = n1 + n2;
                max = Math.max(len, max)
            }
        }
    }

    return max;
};

/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    let pre = 0;
    const prefixSum = [0];

    for(const c of s){
        if(c === "0"){
            pre += 1;
        }
        prefixSum.push(pre);
    }

    let post = 0;
    let max = 0;

    for(let i = s.length - 1; i > 0; i--){
        if(s[i] === "1"){
            post += 1;
        }

        const current = prefixSum[i] + post;

        max = Math.max(max, current)
    }

    return max;
};

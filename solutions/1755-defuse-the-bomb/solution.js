/**
 * @param {number[]} code
 * @param {number} k
 * @return {number[]}
 */
var decrypt = function(code, k) {
    const output = new Array(code.length).fill(0)
    if(k === 0){
        return output;
    }else{
        const polarity = k > 0 ? 1 : -1;
        k *= polarity;
        for(let i = 0; i < output.length; i++){
            for(let j = 1; j <= k; j++){
                const idx = (i + (j * polarity) + code.length) % code.length;
                output[i] += code[idx];
            }
        }    
    }
    return output;
};

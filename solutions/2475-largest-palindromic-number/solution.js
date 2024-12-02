/**
 * @param {string} num
 * @return {string}
 */
var largestPalindromic = function(num) {
    const counts = {};
    for(const n of num){
        counts[n] = (counts[n] ?? 0) + 1;
    }
    
    let bounded = false;
    let front = "";
    let middle = "";
    let back = "";
    
    for(let i = 10; i >= 0; i--){
        let c = counts[i]
        if(c !== undefined && (i !== 0 || bounded)){
            while(c >= 2){
                bounded = true;
                back = i + back;
                front += i;
                c -= 2;
            };
            if(middle.length === 0 && c > 0){
                middle += i;
            }
        }
    };
    
    const ans = front + middle + back
    if(ans.length === 0){
        return "0"
    }
    return ans;
};

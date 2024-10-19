/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    let s = ["0"];
    
    for(let i = 1; i <= n; i++){
        let next = invert(s).reverse();        
        s.push("1");
        s = s.concat(next);
        
        // console.log(s.join(""));

    
        if(s.length > k-1){
            return s[k-1];
        }
    }
};

function invert(x){
    const inverted = [];
    for(const item of x){
        if(item === "0"){
            inverted.push("1");
        }else{
            inverted.push("0");
        }
    }
    return inverted;
}

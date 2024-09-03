/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    
    
    s = s.split("").map(el => el.charCodeAt(0) - 96).join("");
    
    
    function transform(str){
        return str.split("").reduce((a,e) => parseInt(e) + a, 0).toString();
    }
    
    for(let i = 0; i < k; i++){
        s = transform(s)
    }
    
    return parseInt(s);
};

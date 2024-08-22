/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    let x = num.toString(2).split("")
    x = x.map(el => el === "1" ? "0" : "1");
    return parseInt(x.join(""),2)
};

/**
 * @param {string} s
 * @return {boolean}
 */
const alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
var isPalindrome = function(s) {
    s = s.toLowerCase().split('').filter(el => alpha.includes(el));
    return s.join('') === s.reverse().join('');
};  
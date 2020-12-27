/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    let a = s.slice(0, s.length / 2).toLowerCase();
    let b = s.slice(s.length / 2, s.length).toLowerCase();
    
    a = a.split('').filter(el => 'aeiou'.includes(el));
    b = b.split('').filter(el => 'aeiou'.includes(el));
    return (a.length === b.length)
};
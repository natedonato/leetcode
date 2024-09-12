/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    const s = new Set(allowed);
    return words.filter(el => !el.split("").some(c => !s.has(c))).length;


    
};

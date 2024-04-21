/**
 * @param {string[]} strs
 * @return {string[][]}
 */

const aCode = "a".charCodeAt(0);

var groupAnagrams = function(strs) {
    
    // make output array
    
    // make counts of strings
    
    // group equal counts
    
    const counts = {};
    
    for(const str of strs){
        counts[str] = new Array(26).fill(0);
        
        for(let i = 0; i < str.length; i++){
            const char = str[i];
            const code = char.charCodeAt(0) - aCode;
            counts[str][code] += 1;
        };
    };

    const serials = {};
    
    for(const str of strs){
        let serial = counts[str].join(",");
        if(serials[serial] === undefined){
            serials[serial] = [];
        }
        serials[serial].push(str);
    }
    
    return Object.values(serials);
};

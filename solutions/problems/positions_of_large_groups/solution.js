/**
 * @param {string} s
 * @return {number[][]}
 */
var largeGroupPositions = function(s) {
    if(s.length < 3){return []};
    
    let current = s[0];
    let start = 0;
    let collection = [];
    
    for(let i = 0; i < s.length; i++){
        if(s[i] !== current || (i === s.length - 1 && s[i] === current) ){
            let  end = i-1;
            if( i === s.length - 1 && s[i] === current){
                end = i;
            }
            const dif = end - start; 
            if(dif >= 2){
                collection.push([start, end]);
            }
            current = s[i];
            start = i;
        }
    }
    return collection;
};
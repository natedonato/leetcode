/**
 * @param {number[]} arr
 * @param {number[][]} queries
 * @return {number[]}
 */
var xorQueries = function(arr, queries) {
    const prefix = [0];
    let pre = 0
    for(const el of arr){
        pre ^= el;
        prefix.push(pre)

    }
    
    
    console.log(prefix)
    
    const output = queries.map((el) => prefix[el[0]] ^ prefix[el[1]+1])
                                
    return output;

};

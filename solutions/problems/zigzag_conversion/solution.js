/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if(numRows <= 1){
        return s
    }
    let rows = new Array(numRows).fill(0).map(el => new Array())
    
    let r = 0;
    let dir = 1;
    
    for(let i = 0; i < s.length; i++){
        rows[r].push(s[i]);
        r += dir;
        
        if(r === 0){
            dir = 1
        }
        if(r === numRows-1){
            dir = -1
        }
        
        
    }
    
    let str = ""
    rows.forEach(row => str += row.join(""))
    
    return str
};
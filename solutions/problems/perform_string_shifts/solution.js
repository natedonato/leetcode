/**
 * @param {string} s
 * @param {number[][]} shift
 * @return {string}
 */
var stringShift = function(s, shift) {
    let total_offset = 0
    
    shift.forEach(item => {
        let [direction, amount] = item;
        
        if(direction === 0){
            total_offset -= amount;
        }else{
            total_offset += amount;
        }
    })
    
    total_offset = total_offset % s.length;
    
    return stringShifter(total_offset, s)
    
    function stringShifter(int, string){
        string = string.split('')
        if(int === 0){
            return string.join('')
        }else if(int > 0){
            for(let i = 0; i < int; i++){
                string.unshift(string.pop())
            }
        }else{
           for(let i = 0; i > int; i--){
                string.push(string.shift())
            }
        }
        
        string = string.join('');
        return string;
    }
};
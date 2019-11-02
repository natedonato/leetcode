/**
 * @param {number[]} arr
 * @return {number[]}
 */
var transformArray = function(arr) {
    let changed = true;
    let last = arr;
    while(changed === true){
        changed = false;
        let next = last.slice(0);
        for(let i = 1; i < last.length - 1; i++){            
            if((last[i-1] > last[i]) && (last[i+1] > last[i])){
                next[i] += 1;
                changed = true;
            }else if(last[i-1] < last[i] && last[i+1] < last[i]){
                next[i] -= 1;
                changed = true;
            }
        }
        last = next;
    }
    return last;
};
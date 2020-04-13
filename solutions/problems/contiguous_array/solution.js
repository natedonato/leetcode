/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    let current_count = 0;
    let current_max = 0
    let map = {0: -1};
    
    nums.forEach((num, idx) => {
        if(num === 0){
            current_count -= 1;
        }else{
            current_count += 1;
        }
        
        if(map[current_count] === undefined){
            map[current_count] = idx
        }else{
            let length = idx - map[current_count]
            if(length > current_max){current_max = length}
        }
    })
        
    return current_max
};
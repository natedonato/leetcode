/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const set = new Set();
    
    for(const num of nums){
        set.add(num);
    }
    
    let max = 0;
    for(let num of set){
        if(set.has(num - 1)){
            continue;
        }
        
        let run = 0;
        while(set.has(num)){
            run += 1;
            num += 1;
        }
        
        if(run > max){
            max = run
        }
    }
    
    return max;
};

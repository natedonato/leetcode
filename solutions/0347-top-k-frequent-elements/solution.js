/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map();
    
    for(const num of nums){
        if(!map.has(num)){
            map.set(num, 0)
        }
        map.set(num, map.get(num) + 1);
    }
    
    let buckets = new Array(nums.length + 1).fill(0).map(el => new Array())
    
    for(let [key,val] of map.entries()){
        buckets[val].push(key);
    }
    
    let output = [];
    let i = 1;
    while(output.length < k){      
        const bucket = buckets[buckets.length - i];
        for(item of bucket){
            output.push(item)
        }
        i += 1;
    }
    
    return output
};

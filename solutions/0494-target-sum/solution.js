/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function(nums, target) {
    let count = 0;
    
    const memo = new Map();
    
    count = dfs(0,0)
    
    function dfs(sum, i){
        const key = `${sum}:${i}`
        const recall = memo.get(key)
        if(recall !== undefined){
            return recall;
        }
        
        let first = nums[i];
        let subCount = 0
        
        if(i === nums.length - 1){
            if(sum + first === target){
                subCount += 1;
            }
            if(sum - first === target){
                subCount += 1;
            }    
        }else{
            subCount += dfs(sum - first, i + 1);
            subCount += dfs(sum + first, i + 1);    
        }
        memo.set(key, subCount);
        return subCount;
    }
    
    return count;
    
};

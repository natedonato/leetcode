/**
 * @param {number[]} nums
 * @param {number} maxOperations
 * @return {number}
 */
var minimumSize = function(nums, maxOperations) {
    
    
    let l = 1;
    let r = Math.max(...nums);
    
    while(l < r){
        let mid = l + Math.floor((r - l) / 2);

        if(testPossible(mid)){
            r = mid;
        }else{
            l = mid + 1;
        }
    }
    
    return l;
    
    function testPossible(targetSize){
        let ops = 0;
        for(const num of nums){
          ops += Math.ceil(num / targetSize) - 1;
        }
        
        return ops <= maxOperations;
    }
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function(nums) {
    let max = -1;
    const seenNeg = new Map();
    const seenPos = new Map();
    
    for(let i = 0; i < nums.length; i++){
        let el = nums[i];
        
        if(el < 0){
            seenNeg.set(-el, true);
            if(seenPos.get(-el) === true){
                max = Math.max(-el, max);
            }
        }else{
            seenPos.set(el, true);
            if(seenNeg.get(el) === true){
                max = Math.max(el, max);
            }   
        }
    }

    return max;
};

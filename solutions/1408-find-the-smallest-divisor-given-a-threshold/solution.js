/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function(nums, threshold) {
   let l = 1;
   let r = Math.max(...nums);

    while(l < r){
        let mid = Math.floor((r-l) / 2) + l;

            if(test(mid)){
                r = mid;
            }else{
                l = mid + 1;
            }
    }
    return l;
    
    function test(divisor){
        let sum = 0;
        for(const n of nums){
            sum += Math.ceil(n / divisor)
        }
        if(sum <= threshold){
            return true;
        }
        return false;
    };

};

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSquareStreak = function(nums) {
    const s = new Set(nums);
    let longest = -1;
    
    for(let num of nums){
        let streak = 1;
        while(s.has(num * num)){
            streak += 1
            num *= num;
        }
        if(streak >= 2){
            longest = Math.max(longest,streak);
        }
    }
    
    return longest;
};

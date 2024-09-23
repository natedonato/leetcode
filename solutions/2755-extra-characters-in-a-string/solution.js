/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {number}
 */
var minExtraChar = function(s, dictionary) {
    const set = new Set(dictionary);
    const l = s.length;
    const memo = new Map();
    
    function dp(start){
        if(start === l){
            return 0;
        }
        
        if(memo.has(start)){
            return memo.get(start);
        }
        
        // character left over
        let answer = dp(start+1) + 1
        
        for(let end = start; end < l; end++){
            const subString = s.slice(start, end + 1);
            if(set.has(subString)){
                answer = Math.min(answer, dp(end + 1))
            }
        }
        
        memo.set(start, answer);
        return answer;        
    }
    
    return dp(0);
};

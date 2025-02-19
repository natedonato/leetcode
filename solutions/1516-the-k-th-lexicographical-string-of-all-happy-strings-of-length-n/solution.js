/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getHappyString = function(n, k) {
    let count = 0;

    return btrack([]);

    // recursively make string
    function btrack(s){
        // if string is target length, increment our count
        if(s.length === n){
            count += 1
            if(count === k){
                return s.join("")
            }else{
                return "";
            }

        }
        const last = s[s.length - 1];

        for(const char of "abc"){
            if(char !== last){
                s.push(char);
                const res = btrack(s);
                if(res !== ""){
                    return res;
                }
                s.pop();
            }
        }

        return "";
    }
};

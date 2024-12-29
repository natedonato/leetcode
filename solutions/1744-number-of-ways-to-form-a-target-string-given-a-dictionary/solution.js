/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var numWays = function (words, target) {
    const memo = new Map();

    let max = 0;
    const frequencies = [];


    let inBounds = true;

    let i = 0;

    while(inBounds){
        inBounds = false;
        
    
        for (let s = 0; s < words.length; s++) {
            const word = words[s];

            if (word.length > i) {
                inBounds = true;
                max = i

                while(frequencies.length <= i){
                    frequencies.push(new Map());
                }

                frequencies[i].set(word[i], (frequencies[i].get(word[i]) ?? 0) + 1)
            }
        }
        i += 1;
    }

    return dp(0, 0);

    function dp(i, j) {
        const key = "" + i + "," + j;
        if(memo.has(key)){
            return memo.get(key);
        }
        
        const nextChar = target[j];

        if (j === target.length) {
            return 1;
        }

        if(i > max){
            return 0
        }


        let ans = 0;

        let count = frequencies[i].get(nextChar) ?? 0

        if (count > 0) {
            ans += count * dp(i + 1, j + 1);
        }

        ans += dp(i + 1, j)
        
        ans = ans % ((10 ** 9) + 7)

        memo.set(key, ans)
        return ans;
    }
};

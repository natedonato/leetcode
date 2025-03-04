/**
 * @param {number} n
 * @return {boolean}
 */
var checkPowersOfThree = function(n) {
    return btrack(0, n)
};


function btrack(pow, target){
    if(target < 0){
        return false;
    }

    if(target === 0){
        return true
    }

    for(let i = pow; i <= 15; i++){
        res = btrack(i + 1, target - 3**i)
        if(res === true){
            return true
        }
    }

    return false;
}

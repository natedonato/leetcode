/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let visited = {};
    while(n !== 1){
        if(visited[n]){
            return false
        }
        visited[n] = true;
        n = n.toString().split('');
        
        let squareSum = 0;
        n.forEach(digit =>
                 squareSum += digit * digit);
        n = squareSum;
    }
    return true;
};
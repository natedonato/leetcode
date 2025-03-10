/**
 * @param {number[]} p1
 * @param {number[]} p2
 * @param {number[]} p3
 * @param {number[]} p4
 * @return {boolean}
 */
var validSquare = function(p1, p2, p3, p4) {
    const arr = [p1,p2,p3,p4].sort((a, b) => {
        if(a[0] === b[0]){
            return a[1] - b[1]
        }else
            return a[0] - b[0]
    })

    function dist(p1,p2){
        const dx = p1[0] - p2[0]
        const dy = p1[1] - p2[1]
        return dx ** 2 + dy ** 2
    }

    if(
        dist(arr[0],arr[1]) !== 0 &&
        dist(arr[0],arr[1]) === dist(arr[1], arr[3]) &&
        dist(arr[1], arr[3]) === dist(arr[3], arr[2]) &&
        dist(arr[3], arr[2]) === dist(arr[2], arr[0]) &&
        dist(arr[0],arr[3]) === dist(arr[1],arr[2])  
    ){
        return true
    }else{
        return false
    }
};
  

/**
 * @param {number} n
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var checkValidCuts = function(n, rectangles) {
    rectangles.sort((a,b) => a[0] - b[0])

    let count = 0
    let prev = rectangles[0][2];
    for(let i = 0; i < rectangles.length; i++){
        const nextMin = rectangles[i][0]
        const nextMax = rectangles[i][2]
        if(prev <= nextMin){
            count += 1
            if(count >= 2){
                return true;
            }
        }
        if(nextMax > prev){
            prev = nextMax
        }
    }

    rectangles.sort((a,b) => a[1] - b[1])

    count = 0
    prev = rectangles[0][3];
    for(let i = 0; i < rectangles.length; i++){
        const nextMin = rectangles[i][1]
        const nextMax = rectangles[i][3]
        if(prev <= nextMin){
            count += 1
            if(count >= 2){
                return true;
            }
        }
        if(nextMax > prev){
            prev = nextMax
        }
    }


    return false
};

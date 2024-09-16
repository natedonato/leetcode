/**
 * @param {string[]} timePoints
 * @return {number}
 */
var findMinDifference = function(timePoints) {
    timePoints.sort()
    timePoints = timePoints.map(el =>{
        el = el.split(":")
        let mins = parseInt(el[1]) + parseInt(el[0]*60)
        
        return mins;
    })

    timePoints.push(timePoints[0]+ (24*60))

    let dif = Infinity;
    
    let last = timePoints[0]
    for(let i = 1; i< timePoints.length; i++){
        const current = timePoints[i]
        dif = Math.min(current - last, dif)
        last = current;
    }
    return dif;
};

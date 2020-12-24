/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {
    let p = points.sort((a,b) => a[0]-b[0]).map(el => el[0])
    
    let dif = 0;
    for(let i = 0; i < points.length - 1; i++){
        let area = p[i+1] - p[i]
        if(area > dif){
            dif = area;
        }
    }
    return dif
};
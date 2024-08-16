/**
 * @param {number[][]} arrays
 * @return {number}
 */
var maxDistance = function(arrays) {
    let distance = 0;
    let min = arrays[0][0];
    let max = arrays[0][arrays[0].length - 1];
    
    for(let i = 1; i < arrays.length; i++){
        let newMin = arrays[i][0];
        let newMax = arrays[i][arrays[i].length-1];
        
        distance = Math.max(Math.abs(newMax - min), Math.abs(max - newMin), distance);
        
        if(newMin < min){
            min = newMin;
        }
        
        if(newMax > max){
            max = newMax;
        }
    }
    
    return distance;
};

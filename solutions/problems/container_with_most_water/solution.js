/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxArea = 0;
    for(let i = 0; i < height.length -1; i++){
        for(let j = 1; j < height.length; ++j){
            if(j > i){
                let area = (j-i) * Math.min(height[i], height[j]);
                if(area > maxArea){
                    maxArea = area
                }
            }
        }
    }
    return maxArea;
};
/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    let heights2 = [...heights]
    let swapped = true;
    
    while(swapped){
        swapped = false;
        for(let i = 0; i < heights.length - 1; i++){
            if(heights[i] > heights[i+1]){
                swapped = true;
                [heights[i], heights[i+1]] = [heights[i+1],heights[i]]
            }   
        }        
    }
    
    let count = 0;
    for(let i = 0; i < heights.length; i++){
        if(heights[i] !== heights2[i]){
            count += 1;
        }
    }
    
    return count;
};

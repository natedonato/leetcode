/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    let floodColor = image[sr][sc];
    if(color === floodColor){return image}
    let queue = [[sr, sc]];
    
    
    while(queue.length > 0){
        let current = queue.shift();
        
        image[current[0]][current[1]]  = color;
        
        if(current[0] + 1 < image.length){
            if(image[current[0] +1][current[1]] === floodColor){
                queue.push([current[0] +1,current[1]])
            }   
        }
        
        if(current[0] - 1 >= 0){
           if(image[current[0] - 1][current[1]] === floodColor){
                queue.push([current[0] - 1,current[1]])
            } 
        }
        
                
        if(current[1] + 1 < image[0].length){
            if(image[current[0]][current[1] +1] === floodColor){
                queue.push([current[0],current[1]+1])
            }   
        }
        
                   
        if(current[1] - 1 >= 0){
            if(image[current[0]][current[1] - 1] === floodColor){
                queue.push([current[0],current[1] - 1])
            }   
        }
    }
    
    return image;
};
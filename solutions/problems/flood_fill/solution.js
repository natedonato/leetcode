/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    let oldColor = image[sr][sc];
    let visited = {};
    
    const fill = (x,y) => {
        visited[`${x},${y}`] = true;
        if(image[x][y] === oldColor){
            image[x][y] = newColor;
            
            if(x-1 >= 0){
                if(image[x-1][y] === oldColor && !visited[`${x-1},${y}`]){
                    fill(x-1,y)
                }
            }
            if(x + 1 < image.length){
                 if(image[x+1][y] === oldColor  && !visited[`${x+1},${y}`]){
                    fill(x+1,y)
                }
            }
            if(y-1 >= 0){
                 if(image[x][y-1] === oldColor && !visited[`${x},${y-1}`]){
                    fill(x,y-1)
                }
            }
            if(y + 1 < image[0].length){
                if(image[x][y+1] === oldColor && !visited[`${x},${y+1}`]){
                    fill(x,y+1)
                }
            }
        }   
    }
    
    fill(sr, sc)

    return image;
};
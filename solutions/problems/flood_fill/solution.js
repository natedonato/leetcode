/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    let oldColor = image[sr][sc];
    if(oldColor === color){
        return image;
    }else{
        image[sr][sc] = color;
    }

    let queue = [[sr, sc]];

    while(queue.length > 0){
        let [sr, sc] = queue.shift();
        if(sr > 0){
            if(image[sr-1][sc] === oldColor){
                image[sr-1][sc] = color;
                queue.push([sr-1,sc])
            }
        }
        if(sr < image.length - 1){
            if(image[sr+1][sc] === oldColor){
                image[sr+1][sc] = color;
                queue.push([sr+1,sc])
            }
        }
        if(sc > 0){
            if(image[sr][sc-1] === oldColor){
                image[sr][sc-1] = color;
                queue.push([sr,sc-1])
            }
        }
        if(sc < image[0].length - 1){
            if(image[sr][sc+1] === oldColor){
                image[sr][sc+1] = color;
                queue.push([sr,sc+1])
            }
        }
    }


    return image;
};


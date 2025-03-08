/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function(blocks, k) {
    let white_count = 0
    let best = k

    for(let i = 0; i < blocks.length; i++){
        if(blocks[i] === "W"){
            white_count += 1;
        }

        if(blocks[i - k] === "W"){
             white_count -= 1;
        }

        if(i >= k - 1 && best > white_count){
            best = white_count
        }
    }

    return best;
};

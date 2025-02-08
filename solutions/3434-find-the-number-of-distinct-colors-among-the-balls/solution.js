/**
 * @param {number} limit
 * @param {number[][]} queries
 * @return {number[]}
 */
var queryResults = function(limit, queries) {
    let distinctColorCount = 0

    const ballMap = new Map();
    const colorCounts = new Map();

    const output = []

    for(const [ball, color] of queries){
        const ballPrevColor = ballMap.get(ball);
        const colorPrevCount = colorCounts.get(color);
        
        // set ball to new color
        ballMap.set(ball, color)

        // ball has changed color, so decrement old color count
        if(ballPrevColor !== undefined && ballPrevColor !== color){
            let oldCount = colorCounts.get(ballPrevColor)
            colorCounts.set(ballPrevColor, oldCount - 1)

            // if no more of previous color, decrement count
            if(oldCount === 1){
                distinctColorCount -= 1
            }
        }

        
        if(ballPrevColor !== color){
            const count = colorCounts.get(color)

            if(count === 0 || count === undefined){
                distinctColorCount += 1;
            }

            colorCounts.set(color, (count ?? 0) + 1)

        }
        
        output.push(distinctColorCount)
    }

    return output
};

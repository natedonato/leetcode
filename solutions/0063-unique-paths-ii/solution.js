/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    const dp = new Array(obstacleGrid.length).fill(0).map(el => new Array(obstacleGrid[0].length).fill(0));
    if(obstacleGrid[0][0] === 1){
        return 0;
    }
    
    dp[0][0] = 1;

    obstacleGrid[0][0] = 1;
    
    for(let i = 0; i < obstacleGrid.length; i++){
        for(let j = 0; j < obstacleGrid[0].length; j++){
            let paths = 0;

            if(i > 0){
                paths += dp[i-1][j];
            }
            if(j > 0){
                paths += dp[i][j-1];
            }
            
            if(obstacleGrid[i][j] !== 1){
                dp[i][j] = paths;                
            }
        }
    }
        
    return dp[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
};

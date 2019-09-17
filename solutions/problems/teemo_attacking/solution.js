/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    totalPoisonTime = 0;
    
    for(let i = 0; i < timeSeries.length; i++){
        if(timeSeries[i+1] && timeSeries[i+1]-timeSeries[i] < duration){
            totalPoisonTime += timeSeries[i+1]-timeSeries[i]
        }else{
            totalPoisonTime += duration
        }
    }
    return totalPoisonTime
};
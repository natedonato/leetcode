/**
 * @param {number[][]} times
 * @param {number} targetFriend
 * @return {number}
 */
var smallestChair = function(times, targetFriend) {
    let t = times[targetFriend];
    const chairs = new Array(times.length);
    times.sort((a,b) => a[0]-b[0]);
    
    // console.log(times);
    
    for(const time of times){
        const arrival = time[0];
        const departure = time[1];
        // console.log(arrival,departure)
        
        
        for(let i = 0; i < chairs.length; i++){
            // console.log(chairs);
            if(!chairs[i] || chairs[i] <= arrival){
                chairs[i] = departure;
                if(time === t){
                    return i;
                }
                break;
            }
        }   
    }
};

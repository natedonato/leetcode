/**
 * @param {number} candies
 * @param {number} num_people
 * @return {number[]}
 */
var distributeCandies = function(candies, num_people) {
    let output = new Array(num_people).fill(0);

    let i = 1;
    while(candies > 0){
        let next = i;
        if(next >= candies){
            next = candies;
        }        
        output[(i-1) % num_people] += next;
        ++i;
        candies = candies - next;
    }
    
    return output;
};
/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    people = people.sort((a,b) => a - b);
    
    let l = 0;
    let r = people.length -1;
    let boats = 0;
    
    while(l < r){
        boats += 1;
        if(people[l] <= limit - people[r]){ // if a small person can fit in a boat
            l++;
        }
        
        r--;
    }
    
    if(l === r){
        boats += 1;
    }
    
    return boats;
};

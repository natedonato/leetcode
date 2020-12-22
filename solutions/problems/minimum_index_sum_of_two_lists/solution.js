/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    let indexes = {};
    list1.forEach((item, idx) =>{
        indexes[item] = idx;
    })
    
    let best = ["invalid"]
    let bestIdx = Infinity
    
    list2.forEach((item, idx) => {
        let idx1 = indexes[item];
        
        if(idx1 !== undefined && idx1 + idx < bestIdx){
            best = [item];
            bestIdx = idx1 + idx 
        }else if(idx1 !== undefined && idx1 + idx === bestIdx){
            best.push(item);
        }
    })
    
    return (best)
};
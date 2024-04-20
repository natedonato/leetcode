/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
    let currentFruits = [];
    const lastSeen = {};
    let max = 0

    let l = 0;
    let r = 0;

    while(r < fruits.length){
        let current = fruits[r];
        lastSeen[current] = r;


        if(currentFruits.length < 2 && !currentFruits.includes(current)){
            currentFruits.push(current);
        }

        if(!currentFruits.includes(current)){
            currentFruits = currentFruits.sort((a,b) => lastSeen[b] - lastSeen[a]);

            let oldFruit = currentFruits.pop();
            l = lastSeen[oldFruit] + 1;
            currentFruits.push(current);
        }

        max = Math.max(max, r - l + 1);
        r++;
    }


    return max
};


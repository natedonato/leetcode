/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxKelements = function(nums, k) {
    const q = new MaxPriorityQueue();
    
    for(const num of nums){
        q.enqueue(num);
    }
    
    
    let score = 0;
    for(let i = 0; i < k; i++){
        let val = q.dequeue().element;
        score += val;
        val = Math.ceil(val / 3);
        q.enqueue(val);
    }
    
    return score;
};

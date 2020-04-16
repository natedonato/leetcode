/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
    this.heap = nums.slice(0,k).sort((a,b)=>{return a-b})
    this.k = k
    
    for(let i = k; i < nums.length; i++){
        this.add(nums[i])
    }
    };
/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
        
    if(val < this.heap[0] && this.heap.length == this.k){
        return this.heap[0]
    }else{
        if(this.heap.length < this.k){
        this.heap.push(val)
            }else{
        this.heap[0] = val};
        this.heap = this.heap.sort((a,b)=>{return a-b})
        return this.heap[0];
    }
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */
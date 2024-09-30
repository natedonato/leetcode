/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.stack = new Array(maxSize);
    this.i = 0;
    this.max = maxSize;
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if(this.i < this.max){
    this.stack[this.i] = x;
    this.i++;
}
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    if(this.i=== 0){
        return -1
    }
    this.i -= 1;
    return this.stack[this.i];
    
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    k = Math.min(k, this.i);
    for(let i = 0; i < k; i++){
        this.stack[i] += val;
    }
};

/** 
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */

/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.stack = [];
    this.minimums = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.stack.push(x);
    if(this.minimums.length === 0){
        this.minimums.push(x);
    }else{
        this.minimums.push(Math.min(x, this.minimums[this.minimums.length-1]));
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.minimums.pop();
    this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length -1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minimums[this.minimums.length -1];
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
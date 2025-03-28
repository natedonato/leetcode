
var MinStack = function() {
    this.stack = [];
    this.mins = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack.push(val);
    
    if(this.mins.length === 0){
        this.mins.push(val);
    }else{
        let next = Math.min(this.mins[this.mins.length - 1], val)
        this.mins.push(next);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.mins.pop();
return this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.mins[this.mins.length - 1];
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

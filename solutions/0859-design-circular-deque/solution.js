/**
 * @param {number} k
 */
var MyCircularDeque = function(k) {
    this.queue = new Array(k + 1).fill(-1);
    this.front = 0;
    this.last = 1;
    
    this.increase = (p) => {
        p += 1;
        p %= (k + 1);
        return p;
    }
    
    this.decrease = (p) => {
        p -= 1;
        if(p === -1){
            p = k;
        }
        return p;
    }
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function(value) {
    if(this.isFull()){
        return false;
    }else{
        this.queue[this.front] = value;
        this.front = this.decrease(this.front);
        return true;
    }
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function(value) {
    if(this.isFull()){
        return false;
    }else{
        this.queue[this.last] = value;
        this.last = this.increase(this.last);
        return true;
    }
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function() {
    if(this.isEmpty()){
        return false;
    }else{
        this.front = this.increase(this.front);
        this.queue[this.front] = -1;
        return true;
    }
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function() {
    if(this.isEmpty()){
        return false;
    }else{
        this.last = this.decrease(this.last);
        this.queue[this.last] = -1;
        return true;
    }
    
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function() {
    if(this.isEmpty()){
        return -1
    }else{
        return this.queue[this.increase(this.front)];
    }
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function() {
    if(this.isEmpty()){
        return -1
    }else{
        return this.queue[this.decrease(this.last)];
    }
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function() {
    return this.increase(this.front) === this.last
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function() {
    return (this.front === this.last)
};

/** 
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */

var TimeLimitedCache = function() {
    this.cache = {};
    
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    if(!this.cache[key]){
        const dId = setTimeout(() => {
            delete(this.cache[key]);
        }, duration)
        this.cache[key] = {value: value, timeout: dId};
        return false;
    }else{
        clearInterval(this.cache[key].timeout);

        const dId = setTimeout(() => {
            delete(this.cache[key]);
        }, duration)

        this.cache[key] = {value: value, timeout: dId};
        return true;
    }

};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.cache[key] ? this.cache[key].value : -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.cache).length;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
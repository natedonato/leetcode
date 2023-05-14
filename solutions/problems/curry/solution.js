/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    const params = [];
    return function curried(...args) {
        for(const arg of args){
            params.push(arg);
        }

        if(params.length >= fn.length){
            return fn(...params);
        }else{
            return curried.bind(this);
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
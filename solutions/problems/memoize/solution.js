/**
 * @param {Function} fn
 */
function memoize(fn) {
    let mem = {};

    return function(...args) {
        let key = args.join(',');
        if(mem[key] !== undefined){
            return mem[key]
        }else{
            let res = fn(...args);
            mem[key] = res;
            return res;
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
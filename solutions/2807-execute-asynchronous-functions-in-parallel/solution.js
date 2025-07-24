/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((res, rej) =>
        {
            const out = new Array(functions.length).fill(0);
            let finished_count = 0
            for(let i = 0; i < functions.length; i++){
                let fn = functions[i];
                fn().then((fn_result) => {
                    out[i] = fn_result;
                    finished_count += 1;

                    if(finished_count === functions.length){
                        res(out);
                    }
                }).catch(err => rej(err));
            }
        }
    )
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */

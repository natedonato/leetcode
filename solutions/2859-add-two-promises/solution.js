/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return new Promise( (res, rej) =>{
        Promise.all([promise1, promise2]).then(res1 => res(res1[0] + res1[1])).catch(err => rej(err))
    })
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */

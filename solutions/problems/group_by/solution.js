/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const group = {};

    this.forEach(el => {
        const key = fn(el);
        if(group[key] === undefined){
            group[key] = [];
        }
        group[key].push(el);
    });

    return group;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
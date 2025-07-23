/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const out = {}
    out.toBe = (val2) => {
        if (val === val2){
            return true
        }else{
            throw new Error("Not Equal")
        }
    }
    out.notToBe = (val2) => {
        if (val !== val2){
            return true
        }else{
            throw new Error("Equal")
        }
    }
    return out
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */

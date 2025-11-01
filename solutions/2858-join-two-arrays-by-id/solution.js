/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    m = {}
    for(const el of arr1){
        m[el.id] = el
    }
        
    for(const el of arr2){
        if(m[el.id] !== undefined){
            for(const key of Object.keys(el)){
                m[el.id][key] = el[key]
            }
        }else{
            m[el.id] = el
        }
    }

    out = []  
    for(const key of Object.keys(m).sort((a,b) => a - b)){
        out.push(m[key])
    }
    return out
};

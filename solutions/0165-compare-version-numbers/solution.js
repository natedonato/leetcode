/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    version1 = version1.split(".").map(el => parseInt(el))
    version2 = version2.split(".").map(el => parseInt(el))
    
    const l = Math.max(version1.length, version2.length);
    
    for(let i = 0; i < l; i++){
        const v1 = version1[i] ?? 0;
        const v2 = version2[i] ?? 0;
        
        
        if(v1 < v2){
            return -1
        }else if(v2 < v1){
            return 1
        }
    }
    
    return 0
};

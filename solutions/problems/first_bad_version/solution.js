/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {        
        
        let left = 1;
        let right = n;
        while(left < right){
            let mid = Math.floor(((right - left) / 2)) + left;
            
            if(isBadVersion(mid) === false){
                left = mid + 1;   
            }else{
                right = mid;
            };
        };
        return right;
    };
};
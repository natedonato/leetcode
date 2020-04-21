/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * function BinaryMatrix() {
 *     @param {integer} x, y
 *     @return {integer}
 *     this.get = function(x, y) {
 *         ...
 *     };
 *
 *     @return {[integer, integer]}
 *     this.dimensions = function() {
 *         ...
 *     };
 * };
 */

/**
 * @param {BinaryMatrix} binaryMatrix
 * @return {number}
 */
var leftMostColumnWithOne = function(binaryMatrix) {
    let [n, m] = binaryMatrix.dimensions();
    console.log(n, m)
    let leftmost = Infinity;
    let current_j = m - 1;
    
    for(let i = 0; i < n; i++){
        let val = binaryMatrix.get(i, current_j)
        
        while(val === 1){
            if(current_j < leftmost){
                leftmost = current_j
            }
            current_j -= 1;
            val = binaryMatrix.get(i, current_j)

            console.log(i, current_j)
        }
        
        
        
    }
        
    if(leftmost === Infinity){
        return -1
    }
        
    return leftmost;
};

var ProductOfNumbers = function() {
    this.products = [1]
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    if(num === 0){
        this.products = [1]
        return;
    }
    const last = this.products[this.products.length - 1];
    this.products.push(last * num);
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    if(this.products.length <= k){
        return 0;
    }

    return(this.products[this.products.length - 1] / this.products[this.products.length - k - 1])
};

/** 
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */

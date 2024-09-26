
var MyCalendar = function() {
    this.books = [];
};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendar.prototype.book = function(start, end) {
    
   for(const book of this.books){
       let [b1,b2] = book;
       if(start < b2 && end > b1){
            return false           
       }
   }
    this.books.push([start,end])
    return true;

};

/** 
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */

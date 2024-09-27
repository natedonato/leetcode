
var MyCalendarTwo = function() {
    this.bookings = [];
    this.doubleBookings = [];
    
    // if intervals intersect, call this function to make the intersection interval
    this.makeOverlapInterval = (book1, book2) => {
        if(book1[0] > book2[0]){
            return [book1[0],Math.min(book2[1],book1[1])]
        }else{
            return [book2[0],Math.min(book2[1],book1[1])]
        }
        
    }
    
    // search a book collection to find any books that intersect
    this.findOverlaps = (bookings, start,end) => {
        const output = [];
        for(const book of bookings){
            if(start < book[1] && end > book[0]){
                output.push(book);
            }
        }
        return output;
    }
};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendarTwo.prototype.book = function(start, end) {
    if(this.findOverlaps(this.doubleBookings, start,end).length > 0){
        return false;
    }else{
        let intersects = this.findOverlaps(this.bookings, start,end);
        for(const book of intersects){
            this.doubleBookings.push(this.makeOverlapInterval(book, [start,end]))
        }
        this.bookings.push([start,end]);
        return true;
    }
};

/** 
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(start,end)
 */

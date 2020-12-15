/**
 * @param {string} date
 * @return {string}
 */
var reformatDate = function(date) {
    let [day, month, year] = date.split(' ');
    day = day.slice(0, -2);
    
    month = [null, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].indexOf(month);
     
    if(day.length < 2){
        day = '0' + day;
    }
    
    if(month < 10){
        month = '0'+month;
    }
    
    return `${year}-${month}-${day}`
};
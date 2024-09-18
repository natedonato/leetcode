/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    let output = nums.sort(compare).join("")
    
    function compare(a,b){
        
        a = a.toString();
        b = b.toString();
        const temp = a;
        a += b;
        b += temp;
        
        a = parseInt(a);
        b = parseInt(b);
        
        if(a > b){
            return -1;
        }
        else if(b > a){
            return 1;
        }else{
            return 0;
        }
    }
    
    while(output.length > 1 && output[0] === "0"){
        output = output.slice(1);
    }
    
    return output;
};

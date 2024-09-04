/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const stack = [];
    const output = new Array(temperatures.length).fill(0);
    
    for(let i = 0; i < temperatures.length; i++){
        const temp = temperatures[i];
       
        while(stack.length > 0 && stack[stack.length-1][0] < temp){
            let prevDay = stack.pop()[1];        
            output[prevDay] = i - prevDay;
        }  
        
        stack.push([temp,i]);
    }
    
    return output;
};

/**
 * @param {string} start
 * @param {string} target
 * @return {boolean}
 */
var canChange = function(start, target) {
//     let t = 0;
//     let s = 0;
    
//     while(t < target.length){
//         //
//         if(start[s] === target[t]){
//             s++;
//             t++;
//         }else if(target[t] === "R"){
//             return false;
//         }
        
        
//     }
    let i = 0;
    let unpairedL = 0;
    let unpairedR = 0;
    
    for(let i = 0; i < target.length; i++){
        const s = start[i];
        const t = target[i];
    
        
        if(s === "L"){
            if(unpairedR !== 0){
                return false;
            } else {
                unpairedL -= 1;
            }
        }
        
        if(t === "L"){
            if(unpairedR !== 0){
                return false;
            }else{
                unpairedL += 1;                
            }
        }
        
        if(unpairedL < 0){
            return false;
        }
        
        if(s === "R"){
            if(unpairedL !== 0){
                return false;
            }
            unpairedR += 1;
        }
        
        if(t === "R"){
            if(unpairedL !== 0){
                return false;
            }
            unpairedR -= 1;
        }
        
        if(unpairedR < 0){
            return false;
        }
    }
    if(unpairedL !== 0 || unpairedR !== 0){
        return false;
    }
    
    return true;
};

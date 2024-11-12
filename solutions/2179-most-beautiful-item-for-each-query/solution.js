/**
 * @param {number[][]} items
 * @param {number[]} queries
 * @return {number[]}
 */
var maximumBeauty = function(items, queries) {
    items.sort((a,b) => {
        if(a[0] === b[0]){
            return b[1] - a[1];
        }else{
            return a[0] - b[0];
        }
    })
    
    let max = 0;
    for(const item of items){
        if(item[1] > max){
            max = item[1];
        }else{
            item[1] = max;
        }
    }
        
    const output = [];
    
    for(const targetPrice of queries){
        
        // bsearch
        let left = 0;
        let right = items.length - 1;
        
        while(left < right){
            let mid = Math.floor((right - left) / 2) + left;  
            
            if(items[mid][0] >= targetPrice){
                right = mid;   
            }else{
                left = mid + 1;
            }
        }
        
        // left is the first idx with an equal or price than target
        
        if(items[left][0] <= targetPrice){
            output.push(items[left][1])
        }else{
            left -= 1;
            if(left < 0){
                output.push(0);
            }else{
                output.push(items[left][1])
            }
        }
        
        
    }
    
    return output;
};

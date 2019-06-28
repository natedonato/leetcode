var longestCommonPrefix = function (strs) {
    let first = strs.shift();
    if(!first){return ""}
    let i = 0;
    let prefix = "";
    while(i < first.length){
    if(strs.every(el => (
        el[i] === first[i]
        ))){
            prefix += first[i];
            i++;
        }
    else{
        return prefix;
        }
    }
    return prefix;
};
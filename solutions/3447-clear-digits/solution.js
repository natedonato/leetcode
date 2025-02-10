/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function(s) {
    let output = ""
    const nums = "1234567890"

    for(const char of s){
        if(!nums.includes(char)){
            output += char
        }else{
            let r = output.length - 1
            while(nums.includes(output[r])){
                r -= 1
            }
            const temp = output.slice(0,r) + output.slice(r+1, output.length)
            output = temp
        }
    }

    return output
};

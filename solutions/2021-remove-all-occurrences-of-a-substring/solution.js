/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    let output = ""

    let i = 0;
    while(i < s.length){
        const char = s[i]
        output += s[i]
        if(output.slice(output.length - part.length) === part){
            output = output.slice(0, output.length - part.length)
        }
        i += 1
    }

    return output
};

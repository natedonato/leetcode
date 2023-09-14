/**
 * @param {string} s
 * @return {string[]}
 */
var cellsInRange = function(s) {
    let alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let [start, end] = s.split(":");
    let startLetter = start.charAt(0);
    let endLetter = end.charAt(0);
    let startInt = parseInt(start.slice(1))
    let endInt = parseInt(end.slice(1));
    const output = [];

        for(let j = alpha.indexOf(startLetter); j <= alpha.indexOf(endLetter); j++){
    for(let i = startInt; i <= endInt; i++){
            output.push(alpha[j]+i);
        }
    }

    return output;
};

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    s = s.split("")
    let i = 0;
    let j = 0;
    while(i < s.length){
        while(s[j] !==" " && j < s.length){   
            j += 1;
        }
        reverseWord(s,i, j-1);
        j++;
        i = j;
    }
    return s.join("");
};

var reverseWord = function(s,i,j) {
    while(i < j){
        [s[i], s[j]] = [s[j],s[i]];
        i++;
        j--;
    };
}

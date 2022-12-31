/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    s = s.split('');
    let left = 0;
    let right = s.length - 1;
    while(left < right){
        while(left < s.length && !isVowel(s[left])){
            left += 1;
        }
        while(right > 0 && !isVowel(s[right])){
            right -= 1;
        }

        if(left <= right){
            [s[left],s[right]] = [s[right],s[left]]
            left += 1;
            right -= 1;
        }
    }
    
    return s.join("");
};

var isVowel = function (char){
    return'aeiouAEIOU'.includes(char)
}
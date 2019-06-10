
var lengthOfLongestSubstring = function (s) {
    let length = 1;
    if(s.length === 0){
        return 0;
    }
    let substring = s[0];

    for(let i = 1; i < s.length; i++){
        let char = s[i];
        substring = checkForInclusion(substring, char).concat(char);
        if(substring.length > length){
            length = substring.length;
        }
    }
    return length;
};

var checkForInclusion = function (s, c) {
    const index = s.indexOf(c);
    if(index === -1){
        return s;
    }else{
        return s.slice(index + 1);
    }
};

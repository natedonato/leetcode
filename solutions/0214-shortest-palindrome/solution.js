var shortestPalindrome = function (s) {
    const len = s.length;
    for (let i = len; i >= 0; i--) {
        if (isPali(s,0,i-1)) {
            const suffix = s.slice(i, len);
            return suffix.split("").reverse().join("") + s;
        }
    }
    return s;
};


var isPali = function (s,i,j) {
    while (i <= j) {
        if (s[i] != s[j]) return false;
        i++;
        j--;
    }
    return true;
}

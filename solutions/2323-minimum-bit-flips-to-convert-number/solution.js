var minBitFlips = function(start, goal) {
    let dif = start^goal;
    let total = 0;
    while(dif > 0){
        dif &= dif - 1;
        ++total;
    }
    return total;
};

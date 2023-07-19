var minEatingSpeed = function(piles, h) {
    let l = 1;
    let r = Math.max(...piles);

    while(l < r){
        let mid = Math.floor((r - l)/2) + l; 
        if(piles.reduce((acc, el) => Math.ceil(el / mid) + acc, 0) <= h){
            r = mid;
        }else{
            l = mid + 1
        }
    }

    return l;
};

/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    const n = nums.length;
    const s = new Set(nums);

    function randomBin(){
        const out = []
        for(let i = 0; i < n; i++){
            if(Math.random() > 0.5){
                out.push(1)
            }else{
                out.push(0)
            }
        }
        return out.join("");
    }

    let random = randomBin();
    while(s.has(random)){
        random = randomBin();
    }

    return random;
};

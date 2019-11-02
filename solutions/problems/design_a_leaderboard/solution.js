
class Leaderboard{
    constructor(){
        this.scores = {};
    }
}

/** 
 * @param {number} playerId 
 * @param {number} score
 * @return {void}
 */
Leaderboard.prototype.addScore = function(playerId, score) {
    if(this.scores[playerId]){
        this.scores[playerId] += score;
    }else{
        this.scores[playerId] = score;
    }
};

/** 
 * @param {number} K
 * @return {number}
 */
Leaderboard.prototype.top = function(K) {
    let arr = Object.values(this.scores).sort((a,b) => a-b);
    let top = arr.reverse().slice(0, K);
    let sum = 0;
    top.forEach(score => sum += score);
    return sum;
};

/** 
 * @param {number} playerId
 * @return {void}
 */
Leaderboard.prototype.reset = function(playerId) {
    this.scores[playerId] = 0;
};

/** 
 * Your Leaderboard object will be instantiated and called as such:
 * var obj = new Leaderboard()
 * obj.addScore(playerId,score)
 * var param_2 = obj.top(K)
 * obj.reset(playerId)
 */
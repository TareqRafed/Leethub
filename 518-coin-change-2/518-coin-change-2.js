/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */

var change = function(amount, coins) {
    
   
    let dp = new Array(amount + 1).fill(0)
    dp[0] = 1
    
    for(let i =0; i < coins.length; i ++) {
        for(let j = coins[i]; j < dp.length;j ++) {
            dp[j] += dp[j - coins[i]]
        }
    }
            
    return dp[dp.length - 1]
    
};
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices.windows(2).fold(0, |acc, w| acc+(w[1] - w[0]).max(0))
    }
}
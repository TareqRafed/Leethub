impl Solution {
    pub fn xor_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = vec![];
        for i in 0..queries.len() {
            let start = queries[i][0];
            let end = queries[i][1];
            let mut chunk = arr[start as usize];
            for r in start+1..=end {
                chunk = arr[r as usize] ^ chunk
            }
            result.push(chunk);
        }
        result
    }
}
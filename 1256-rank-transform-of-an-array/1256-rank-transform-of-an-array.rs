impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut sorted = arr.clone();
        sorted.sort();
        sorted.dedup();
        let mut ans = arr.clone();
        for i in 0..arr.len() {
            match sorted.binary_search(&arr[i]) {
                Ok(index) => ans[i] = index as i32 + 1,
                _ => println!("Err"),
            }
        }
        ans
    }
}
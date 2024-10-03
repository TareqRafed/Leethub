use std::collections::HashMap;

impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut sorted = arr.clone();
        sorted.sort();
        sorted.dedup();
        let mut ans = arr.clone();
        
        let mut hm: HashMap<i32, i32> = HashMap::new();
        for i in 0..sorted.len() {
            hm.insert(sorted[i], i as i32 +1);
        }

        for i in 0..arr.len() {
            ans[i] = hm[&arr[i]];
        }
        ans
    }
}
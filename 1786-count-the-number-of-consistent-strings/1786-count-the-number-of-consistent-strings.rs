use std::collections::HashMap;

impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let mut allowed_hm = HashMap::new();
        for ch in allowed.chars() {
            allowed_hm.insert(String::from(ch), 1);
        }
        let mut ans: i32 = 0;
        for word in words.iter() {
            let mut count = true;
            for ch in word.chars() {
                if let Some(ex) = allowed_hm.get(&String::from(ch)) {

                } else {
                    count = false;
                    break;
                }
            }
            if count == true {
                ans = ans + 1;
            }
        }
        ans
    }
}
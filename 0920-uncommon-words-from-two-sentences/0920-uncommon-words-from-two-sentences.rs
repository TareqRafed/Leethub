use std::collections::HashMap;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut hm: HashMap<&str, i32> = HashMap::new();
        let as1 = s1.split(" ");
        let as2 = s2.split(" ");
        let mut ans: Vec<String> = vec![];
        for word in as1 {
            let count = hm.entry(word).or_insert(0);
            *count += 1;
        }
        for word in as2 {
            let count = hm.entry(word).or_insert(0);
            *count += 1;
        }

        for (key, value) in &hm {
            if hm[key] == 1 {
                ans.push(key.to_string());
            }
        }
        ans
    }
}
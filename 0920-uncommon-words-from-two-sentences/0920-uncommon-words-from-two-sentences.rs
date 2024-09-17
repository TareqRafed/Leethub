use std::collections::HashMap;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut hm: HashMap<&str, i32> = HashMap::new();
        s1.split(' ').chain(s2.split(' ')).for_each(|s| *hm.entry(s).or_insert(0) += 1);

        hm.iter()
        .filter_map(|(key, val)| match *val == 1 {
            true => Some((*key).to_string()),
            false => None,
        })
        .collect::<Vec<_>>()
    }
}
use std::collections::HashMap;

impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
          let vowels = "aeiou";
          let mut res = 0;
          let mut state: u32 = 0;
          let mut state_map: HashMap<u32, i32> = HashMap::new();
          state_map.insert(0, -1);
          for (i, c) in s.char_indices() {
            if vowels.contains(c) {
                state ^= (1 as u32 + (c as u32) - ('a' as u32));
            }

            if let Some(value) = state_map.get(&(state as u32)) {
                res = res.max(i - (*value as usize));
            } else {
                state_map.insert(state as u32, i as i32);
            }
          }

          res as i32
    }
}
use std::collections::HashMap;

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        let mut cnt: i32 = 0;
        let mut max_l: i32 = 0;
        
        let mut h_map: HashMap<i32, i32> = HashMap::new();
        h_map.insert(0, -1);
        
        for (i, &val) in nums.iter().enumerate() {
            cnt += if val == 1 { 1 } else { -1 };
            match h_map.get(&cnt) {
                Some(strd_ind) => {
                    max_l = std::cmp::max(max_l, i as i32 - strd_ind);
                },
                None => {
                    h_map.insert(cnt, i as i32);
                }
            }
        }
        max_l
    }
}

// [1,1,1,1,0,0,0]
// cnt 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1
// ind 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

// [0, 1]
// cnt  0 -> -1 -> 0 
// ind -1 -> 0 -> 1 
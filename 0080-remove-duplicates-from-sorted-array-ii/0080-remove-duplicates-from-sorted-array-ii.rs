use std::collections::HashMap;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut hm: HashMap<i32, i32> = HashMap::new();

        nums.iter().for_each(|e| *hm.entry(*e).or_insert(0) += 1);
        let mut i: usize = 0;
        while i < nums.len() {
            let count = hm.get(&nums[i]).unwrap();
            if *count > 2 {
                *hm.get_mut(&nums[i]).unwrap() -= 1;
                nums.remove(i);
                println!("{:?} {:?} {:?}", nums[i], i, hm);
                continue;
            }
            i += 1;
        }
        nums.len() as i32
    }
}
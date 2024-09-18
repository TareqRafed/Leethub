use std::collections::HashMap;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i: usize = 0;
        for arrIndex in 0..nums.len() {
            if i < 2 || nums[i-2] != nums[arrIndex] {
                nums[i] = nums[arrIndex];
                i += 1;
            }
        }
        i as i32
    }
}
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut max = nums[0];
        let mut curr_len = 0;
        let mut max_len = 1;

        for i in 0..nums.len() {
            max = std::cmp::max(nums[i], max); 
        }

        for i in 0..nums.len() {
            if nums[i] != max {
                curr_len = 0;
            }
            if nums[i] == max {
                curr_len += 1;
                max_len = std::cmp::max(curr_len, max_len)
            }
        }
        max_len
    }
}
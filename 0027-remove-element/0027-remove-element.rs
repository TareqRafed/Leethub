impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut j: usize = nums.len(); 
        let mut i: usize = 0;
        
        while i < j {
            if nums[i] == val {
                nums.swap(i, j - 1);
                j -= 1;
                continue;
            }
            i += 1
        }
        
        i as i32
    }
}
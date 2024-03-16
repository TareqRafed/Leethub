impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut res: i32 = 0;
        let mut arr_len: i32 = nums.len() as i32;
        let mut temp: Vec<usize> = Vec::new();
        
        for (i, iter_v) in nums.iter().enumerate() {
            if *iter_v == val {
                res += 1;
                temp.push(i);
            }
        }

        for (ind, i_v) in temp.iter().enumerate() {
            nums.remove(*i_v - ind);
        }

        arr_len - res
    }
}
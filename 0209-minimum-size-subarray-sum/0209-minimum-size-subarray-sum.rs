impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut pre_sum = vec![0; nums.len() + 1];
        for i in 0..nums.len() {
            pre_sum[i+1] += nums[i] + pre_sum[i];
        }

        println!("{:?}", pre_sum);

        let mut l_p: usize = 0;
        let mut r_p: usize = 1;
        let mut min_len = pre_sum.len();

        while l_p < r_p && r_p < pre_sum.len() && l_p < pre_sum.len() {
            let mut sum = 0;
            sum = pre_sum[r_p] - pre_sum[l_p];
            if sum >= target {
                min_len = min_len.min((r_p - l_p));
                l_p += 1;
                continue;
            }
            r_p += 1;
        }

        if min_len >= pre_sum.len() { return 0 }
        min_len as i32

    }
}

// t = 7
// nums = 2, 3, 1, 2, 4, 3
// output = 2

// 0........3......5
// 0, 2, 5, 6, 8, 12, 15
// 0, 0, 0, 4, 3, 2 
// .........^------^
//     .           .

// 1,1,1,1,1,1,1,1,1
// 1,2,3,4,5,6,7,8,9
// 0,0,0,0,0,0,0,0,0
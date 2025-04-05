impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        let arr_len = arr.len();
        let mut memo = vec![-1;arr_len];
        fn dfs(arr: Vec<i32>, arr_len: usize, k: i32, i: usize, mut memo: &mut Vec<i32>) -> i32 {
            let mut res = 0;
            let mut cur_sum = 0;
            let mut cur_max = 0;
            if i >= arr_len {
                return 0;
            }
            if memo[i] != -1 {
                return memo[i];
            }

            for j in i..arr_len.min(i+k as usize) {
                cur_max = cur_max.max(arr[j]);
                cur_sum = cur_max * (j-i+1) as i32;
                res = res.max(dfs(arr.clone(), arr_len, k, j+1, &mut memo) + cur_sum)
            }
            memo[i] = res;
            return res;
        };

        return dfs(arr.clone(), arr_len, k, 0, &mut memo);
    }
}
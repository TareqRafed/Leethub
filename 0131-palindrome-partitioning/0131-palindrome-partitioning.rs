impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let mut ans = Vec::new();
        let mut candidates = Vec::new();


        fn dfs(ans: &mut Vec<Vec<String>>, s: &String, candidates: &mut Vec<String>, start: usize) {
            if start == s.len() {
                ans.push(candidates.to_vec());
            }

            for i in start..s.len() {
                let cand = s[start..=i].to_string();
                if !is_pali(cand.clone()) {
                    continue;
                }
                candidates.push(cand);
                dfs(ans, &s, candidates, i+1);
                candidates.pop();
            }
        };

        dfs(& mut ans, &s, &mut candidates, 0);

        

        fn is_pali(s: String) -> bool {
            s.chars().eq(s.chars().rev())
        }

        ans
    }
}
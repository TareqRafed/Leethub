impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let (mut l_p, mut r_p) = (0, s.len() - 1);
        while l_p < r_p {
            s.swap(l_p, r_p);
            l_p += 1;
            r_p -= 1;
        }
    }
}
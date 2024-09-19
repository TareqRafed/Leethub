impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        let (mut i, mut res) = (0, vec![]);
        for i in 0..expression.len() {
            let b = expression.as_bytes()[i];
            if let b'+' | b'-' | b'*' = b {
                let left_res = Self::diff_ways_to_compute(expression[..i].to_string());
                let right_res = Self::diff_ways_to_compute(expression[i + 1..].to_string());
                for left in &left_res { for right in &right_res { res.push(match b {
                    b'+' => left + right, b'-' => left - right, _ => left * right
                })}}
            }}
        if res.is_empty() { vec![expression.parse::<i32>().unwrap()] } else { res }
    }
}
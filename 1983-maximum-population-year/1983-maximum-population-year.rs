impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        let mut years: Vec<i32> = vec![0; 2051];
        
        for log in &logs {
            years[log[0] as usize] += 1;
            years[log[1] as usize] -= 1;
        }

        let mut max_year = 1950;
        // get max index;
        for year in 1950..years.len() {
            years[year] += years[year - 1];
            if years[max_year as usize] < years[year] {
                max_year = year as i32;
            }
        }

        max_year
    }
}
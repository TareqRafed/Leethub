impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        let mut years: Vec<i32> = vec![0; 2051];
        
        for log in &logs {
            for year in log[0]..log[1] {
                years[year as usize] += 1;
            }
        }

        let mut max_year = 1950;
        // get max index;
        for year in 1950..years.len() {
            if years[max_year as usize] < years[year] {
                max_year = year as i32;
            }
        }

        max_year
    }
}
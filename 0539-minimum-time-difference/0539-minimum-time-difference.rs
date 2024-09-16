impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        let mut min = i32::MAX;
        let mut tmp: Vec<i32> = vec![];


        for time in time_points {
            let part: Vec<&str> = time.split(':').collect();
            let hrs: i32 = part[0].parse().unwrap();
            let mins: i32 = part[1].parse().unwrap();
            let count = (hrs * 60) + mins;
            tmp.push(count);
        } 
        tmp.sort();

        for i in 0..tmp.len() - 1 {
            min = std::cmp::min(tmp[i+1] - tmp[i], min); 
        }
        min = std::cmp::min(min, 24 * 60 - tmp.last().unwrap() + tmp[0]);
        min
    }  
}
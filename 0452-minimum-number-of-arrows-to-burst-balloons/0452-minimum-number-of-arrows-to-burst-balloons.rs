impl Solution {
    pub fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
        
        points.sort_unstable_by(|a, b| a[1].cmp(&b[1]));
        
        let mut shots = 0;
        let mut target = points[0][1];
        
        for point in points {
            if point[0] > target && point[1] > target {
                shots += 1;
                target = point[1];
            }
        }
        shots + 1
    }
}

// [1, 6] [2, 8] [7, 12] [10, 16]
// t = 6

//[[1,2],[3,4],[5,6],[7,8]]

// [[1,2],[2,3],[3,4],[4,5]]
// 4 // 1
use std::cmp::Ordering;

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let (mut s, mut e) = (new_interval[0], new_interval[1]);

        let pred = |x| {
            move |i: &Vec<i32>| {
                if i[0] > x {
                    Ordering::Greater
                } else if i[1] < x {
                    Ordering::Less
                } else {
                    Ordering::Equal
                }
            }
        };

        let li = intervals.binary_search_by(pred(s)).unwrap_or_else(|x| x);
        let ri = intervals.binary_search_by(pred(e)).unwrap_or_else(|x| x);

        let l = &intervals[..(li + usize::from(li < intervals.len() && intervals[li][1] < s))];
        let r = &intervals[(ri + usize::from(ri >= intervals.len() || intervals[ri][0] <= e))
            .min(intervals.len())..];

        if l.len() + r.len() != intervals.len() {
            s = s.min(intervals[l.len()][0]);
            e = e.max(intervals[intervals.len() - r.len() - 1][1]);
        }

        vec![l, &vec![vec![s, e]], r].concat()
    }
}

// [[1,3],[6,9]] // [2,5]
//

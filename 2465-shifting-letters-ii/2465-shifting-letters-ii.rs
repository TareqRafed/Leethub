impl Solution {
    pub fn shifting_letters(s: String, shifts: Vec<Vec<i32>>) -> String {
    let mut merged_state: Vec<i32> = vec![0;s.len() + 1];

    for step in &shifts {
        let st = step[0];
        let end = step[1];
        let dir = step[2];
        let amt = if dir == 1 { 1 } else { -1 };
        merged_state[st as usize] += amt;
        merged_state[(end + 1) as usize] -= amt;
    }

    for n in 0..merged_state.len() {
        if n>0 {merged_state[n] += merged_state[n - 1];}
        merged_state[n] %= 26;
        if merged_state[n] < 0 {
            merged_state[n] += 26;
        }

    }


    let mut shifted = s.clone();
    for i in 0..shifted.len() {
        let mut char_to_shift = s.chars().nth(i).unwrap() as u8;
        let base = 'a' as u8;
        let shifted_char_as_byte = ((char_to_shift + merged_state[i] as u8 - base) % 26) + base;
        let new_char = char::from(shifted_char_as_byte);
        shifted.replace_range(i..i+1, &new_char.to_string());
    } 
    shifted
    }
}

// a = 26 
// b 27
// c = 28
// 
// t = 29 - 2

// abc
// shifts[i] = start, end, direction
// [0, 1, 0], [1, 2, 1],  [0,2,1]
// zac - zbd - ace
// [-1, -1, 0] -> [-1, 0, 1] -> [0, 1, 2]
// ace

// x = 20 / 4
// alph = 26
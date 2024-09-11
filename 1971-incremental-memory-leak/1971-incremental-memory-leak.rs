impl Solution {
    pub fn mem_leak(memory1: i32, memory2: i32) -> Vec<i32> {
        let mut mem_state = vec![memory1, memory2];
        let mut leak = 1;
        while mem_state[0] >= 0 as i32 && mem_state[1] >= 0 as i32 {
            if mem_state[1] > mem_state[0] {
                mem_state[1] -= leak; // could go under 0
                if mem_state[1] < 0 {
                    mem_state[1] += leak;
                    break;
                }
            } else {
                mem_state[0] -= leak; // could go under 0
                if mem_state[0] < 0 {
                    mem_state[0] += leak;
                    break;
                }
            }
            leak = leak + 1;
        }
        vec![leak, mem_state[0], mem_state[1]]
        
    }
}
use std::collections::HashMap;
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut total = nums.len() as i32;
        let mut counts:HashMap <i32,i32> = HashMap::new();

        for n in nums{
            counts.entry(n).and_modify(|counter| *counter += 1).or_insert(1);
            if *counts.get(&n).unwrap() > total/2 {
                return n
            }

        }
        -1
    }
}
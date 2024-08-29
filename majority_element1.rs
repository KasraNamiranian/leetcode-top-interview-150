use std::collections::HashMap;
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut candidate = 0;
        let mut votes = 0;
        for n in nums {

                if votes == 0 {
                    candidate = n;
                }
                if candidate == n {
                    votes +=1;
                }
                else{
                    votes -=1;
                }

        }
        candidate


    }
}
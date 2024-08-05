#The answer of leetcode top 1nterview 150 the question number 27 (remove element) written by Kasra Namiranian.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  
                k += 1 
        return k

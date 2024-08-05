#The answer of leetcode top 1nterview 150 the question number 27 (remove element) written by Kasra Namiranian.
#Another answer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        iw = 0
        ir = 0
        while (ir < len(nums)):
            if nums[ir] != val:
                k+=1
                nums[iw] = nums[ir]
                iw+=1
            ir+=1
        return k

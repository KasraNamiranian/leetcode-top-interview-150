class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return  1
        prev = nums[0]
        iw = 1
        k = 1
        for ir in range(1, len(nums)):
            if  nums[ir] != prev:
                k+=1
                nums[iw] = nums[ir]
                prev = nums[iw] 
                iw+=1
        return k
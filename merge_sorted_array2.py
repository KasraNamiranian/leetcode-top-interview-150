#Another answer for leetcode top interview 150 the question number 88 (merged sorted array) written by Kasra Namiranian.
#It's the merge_sorted_array1 written in python.


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        n1p = m - 1
        n2p = n - 1
        wp = m + n -1

        while(wp>=0):
            if (n1p<0):
                nums1[wp] = nums2[n2p]
                wp -= 1
                n2p -= 1
            elif (n2p<0):
                nums1[wp] = nums1[n1p]
                wp -= 1
                n1p -= 1
            elif (nums1[n1p]>nums2[n2p]):
                nums1[wp] = nums1[n1p]
                wp -= 1
                n1p -= 1
            else:
                nums1[wp] = nums2[n2p]
                wp -=1
                n2p -=1



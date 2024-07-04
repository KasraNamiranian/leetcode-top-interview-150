//Another answer for leetcode top interview 150 the question number 88 (merged sorted array) written by Kasra Namiranian.
//It's better than perivious one.

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int n1p = m-1;
    int n2p = n-1;
    int wp = m+n-1;
    while(wp>=0){
        if(n1p < 0)
            nums1[wp--] = nums2[n2p--];
        else if (n2p<0)
            nums1[wp--]=nums1[n1p--];
        else if(nums1[n1p]>nums2[n2p]){
            nums1[wp] = nums1[n1p];
            wp--;
            n1p--;
        }
        else
            nums1[wp--] = nums2[n2p--];
    }

}

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        if (n < m) {
            vector<int> temp;
            temp = nums1;
            nums1 = nums2;
            nums2 = temp;
            m = nums1.size();
            n = nums2.size();
        }
        int offset = (m+n+1) / 2;
        int i = 0;
        int j;
        int imin=0, imax=m;
        if (m == 0) {
            int middle = (m + n) / 2;
            if (n % 2 == 0) {
                return (nums2[middle - 1] + nums2[middle]) / 2.0;
            } else {
                return nums2[middle] * 1.0;
            }
        }
        while(imin <= imax) {
            i = (imin + imax) / 2;
            j = offset - i;
            if (i > 0 && nums1[i-1] > nums2[j]) {
                imax = i - 1;
            } else if (i < m && nums1[i] < nums2[j-1]) {
                imin = i+1;
            } else {
                  int maxleft;
                if (i == 0) {
                    maxleft = nums2[j-1];
                } else if (j == 0) {
                    maxleft = nums1[i-1];
                } else {
                    maxleft = max(nums2[j-1], nums1[i-1]);
                }
                if ((m + n) % 2 == 1) {
                    return maxleft * 1.0;
                }
                int minright;
                if (i == m) {
                    minright = nums2[j];
                } else if (j == n) {
                    minright = nums1[i];
                } else {
                    minright = min(nums2[j], nums1[i]);
                }
                return (minright + maxleft) / 2.0;
            }
        }
        return 1.0;
    }
};
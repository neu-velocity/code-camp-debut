class Solution {
    // binary search
    // TC: O(m+n)
    // SC: O(1)
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len = nums1.length + nums2.length;
        if (len == 0) {
            return 0;
        }
        if (len % 2 == 1) {
            return (double) findKth(nums1, nums2, 0, 0, len / 2 + 1);
        } else {
            return (double) (findKth(nums1, nums2, 0, 0, len / 2) + findKth(nums1, nums2, 0, 0, len / 2 + 1)) / 2;
        }
    }

    private int findKth(int[] nums1, int[] nums2, int p1, int p2, int k) {
        if (p1 >= nums1.length) {
            return nums2[p2 + k - 1];
        }
        if (p2 >= nums2.length) {
            return nums1[p1 + k - 1];
        }

        if (k == 1) {
            return Math.min(nums1[p1], nums2[p2]);
        }

        int mid1 = Integer.MAX_VALUE, mid2 = Integer.MAX_VALUE;
        if (p1 + k / 2 - 1 < nums1.length) {
            mid1 = nums1[p1 + k / 2 - 1];
        }
        if (p2 + k / 2 - 1 < nums2.length) {
            mid2 = nums2[p2 + k / 2 - 1];
        }
        if (mid1 > mid2) {
            return findKth(nums1, nums2, p1, p2 + k / 2, k - k / 2);
        } else {
            return findKth(nums1, nums2, p1 + k / 2, p2, k - k / 2);
        }
    }
}
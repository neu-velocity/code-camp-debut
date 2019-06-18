/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

/**
 * mid = (start + end) / 2; is wrong because when start and end are all about
 * INT_MAX, then (start + end) will be overflow.
 */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
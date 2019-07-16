public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1, end = n;
        while(start+1<n){
            int mid = start+(n-start)/2;
            boolean isMidBad = isBadVersion(mid);
            // boolean isNBad = isBadVersion(n);
            boolean isStartBad = isBadVersion(start);
            if(!isMidBad&&!isStartBad) start = mid;
            else n = mid;

        }
        if(isBadVersion(start)) return start;
        if(isBadVersion(n)) return n;
        return 0;
    }
}
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        int i=0,j=0;
        ArrayList<Integer> list = new ArrayList<>();
        while(i<len1&&j<len2){
            if(nums1[i]<=nums2[j]){
                list.add(nums1[i++]);
            }else{
                list.add(nums2[j++]);
            }
        }
        while(i<len1){
            list.add(nums1[i++]);
        }
        while(j<len2){
            list.add(nums2[j++]);
        }
        if((len1+len2)%2==1){
            return (double)list.get(list.size()/2);
        }
        return ((double)list.get(list.size()/2)+(double)list.get(list.size()/2-1))/2;
    }
}
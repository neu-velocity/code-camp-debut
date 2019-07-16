class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tail(nums.size(), 0);
        int size = 0;
        for(int num: nums) {
            int i = 0;
            int j = size;
            while(i < j) { // find first val > num
                int mid = i + (j - i) / 2;
                if(tail[mid] < num) {
                    i = mid + 1;
                }else{
                    j = mid;
                }
            }
            tail[i] = num;
            if(i == size) {
                size++;
            }
        }
        return size;
    }
};
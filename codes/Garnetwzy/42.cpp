class Solution {
public:
    int trap(vector<int>& height) {
        int i = 0;
        int j = height.size()-1;
        int sum = 0;
        int maxLeft = 0;
        int maxRight = 0;
        while(i <= j) {
            if(height[i] < height[j]) {
                if(height[i] > maxLeft) {
                    maxLeft = height[i];
                    i++;
                }else {
                    sum += maxLeft - height[i];
                    i++;
                }
            }else{
                if(height[j] > maxRight) {
                    maxRight = height[j];
                    j--;
                }else{
                    sum += maxRight - height[j];
                    j--;
                }
            }
        }
        return sum;
    }
};
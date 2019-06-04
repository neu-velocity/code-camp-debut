class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        if(n == 0)
            return 0;
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        stack<int> s;
        for(int i = 0; i < n; i++) {
            while(!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            if(s.empty()) {
                left[i] = -1;
            }else {
                left[i] = s.top();
            }
            s.push(i);
        }
        stack<int> s2;
        for(int i = n-1; i >= 0; i--) {
            while(!s2.empty() && heights[s2.top()] >= heights[i]) {
                s2.pop();
            }
            if(s2.empty()) {
                right[i] = n;
            }else {
                right[i] = s2.top();
            }
            s2.push(i);
        }
        int maxVal = INT_MIN;
        for(int i = 0; i < n; i++) {
            maxVal = max(maxVal, heights[i] * (right[i] - left[i] - 1));
        }
        return maxVal;
    }
};
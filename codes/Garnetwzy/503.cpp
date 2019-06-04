/*
 * @lc app=leetcode id=503 lang=cpp
 *
 * [503] Next Greater Element II
 */
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int maxIndex = 0;
        int maxVal = INT_MIN;
        int startIndex;
        vector<int> ret(nums.size(), 0);
        stack<int> s;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] >= maxVal) {
                maxVal = nums[i];
                maxIndex = i;
            }
        }
        ret[maxIndex] = -1;
        int next = nextIndex(maxIndex, nums.size());
        s.push(nums[maxIndex]);
        while(next != maxIndex) {
            while(!s.empty() && s.top() < nums[next]) {
                s.pop();
            }
            if(s.empty()) {
                ret[next] = -1;
                s.push(nums[next]);
            }else {
                ret[next] = s.top();
                s.push(nums[next]);
            }
            next = nextIndex(next, nums.size());
        }
        return ret;
    }

    int nextIndex(int current, int size) {
        if(current == 0)
            return size-1;
        return current-1;
    }
};


class cmp
{
public:
    bool operator()(pair<int, int> a, pair<int, int> b)
    {
        if(a.second < b.second) {
            return true;
        }else {
            return false;
        }
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> hash;
        vector<int> ret;
        for(int num: nums) {
            hash[num]++;
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> q;
        for(auto it = hash.begin(); it!= hash.end(); it++) {
            q.push(pair<int, int>(it->first, it->second));
        }
        for(int i = 0; i < k; i++) {
            pair<int, int> top = q.top();
            ret.push_back(top.first);
            q.pop();
        }
        return ret;
    }
};
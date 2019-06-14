class cmp
{
public:
    bool operator()(vector<int> p1, vector<int> p2)
    {
        if(p1[0] != p2[0]) {
            return p1[0] < p2[0];
        }else{
            if(p1[2] == p2[2]) {
                if(p1[2] == 1) {
                    return p1[1] > p2[1];
                }else{
                    return p1[1] < p2[1];
                }
            }else{
                return p1[2] == 1 ? true : false;
            }
        }
    }
}; 

class Solution {
public:
    multiset<int> p;
    int maxHeight() {
        if(p.empty())
            return 0;
        return *p.rbegin();
    }
    
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> pointArray;
        vector<vector<int>> ret;
        for(vector<int> building: buildings) {
            pointArray.push_back({building[0], building[2], 1});
            pointArray.push_back({building[1], building[2], 0});
        }
        sort(pointArray.begin(), pointArray.end(), cmp());
        for(vector<int> point: pointArray) {
            if(point[2] == 1) {
                if(point[1] > maxHeight()) {
                    ret.push_back({point[0], point[1]});
                }
                p.insert(point[1]);
            }else {
                p.erase(p.equal_range(point[1]).first);
                if(point[1] > maxHeight()) {
                    ret.push_back({point[0], maxHeight()});
                }
            }
        }
        return ret;
    }
};
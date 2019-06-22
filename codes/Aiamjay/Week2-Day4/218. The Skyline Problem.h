//
// Created by 长夜总有天亮时 on 2019-06-19.
//

#ifndef __218__
#define __218__

#include <iostream>
#include <vector>
#include <math.h>
#include <queue>
#include <set>
#include <map>

using namespace std;

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>> &buildings) {

    }
};

#define none pair<int, int>(-1, -1)

class SegmentTree {
private:
    int *values; // wjcnote 代表这个区间被完全覆盖的次数，0表示没有覆盖, >=1 表示被覆盖
    int *lazy;
    int size;
    int length;
    int result;
    vector<pair<int, int>> change;

    void build_tree(int pos, int begin, int end, int *vals) {
        if (end - begin == 1) {
            size++;
            values[pos] = vals[begin];
            return;
        }
        int mid = (begin + end) / 2;
        build_tree(pos * 2 + 1, begin, mid, vals);
        build_tree(pos * 2 + 2, mid, end, vals);
        values[pos] = max(values[pos * 2 + 1], values[pos * 2 + 2]);
        size++;
    }

    void push_down(int pos, int start, int end) {
        int origin = values[pos];
        values[pos] += lazy[pos];
        if ((origin == 0 && values[pos] == 1) || (origin == 1 && values[pos] == 0))
            change.emplace_back(pair<int, int>(start, end));
        if (pos * 2 + 1 < size) {
            lazy[pos * 2 + 1] = lazy[pos];
            lazy[pos * 2 + 2] = lazy[pos];
        }
        lazy[pos] = 0;
    }

    void _update_range(int pos, int start, int end, int rstart, int rend, int value) {
        if (lazy[pos] != 0) {
            push_down(pos, start, end);
        }

        if (rstart <= start && end <= rend) {
            lazy[pos] = value;
            push_down(pos, start, end);
            return;
        }
        if (rstart >= end || rend <= start)
            return;
        int mid = (start + end) / 2;
        _update_range(pos * 2 + 2, mid, end, rstart, rend, value);
        _update_range(pos * 2 + 1, start, mid, rstart, rend, value);

        int origin = values[pos];
        values[pos] = max(values[pos * 2 + 1], values[pos * 2 + 2]);
        if ((origin == 0 && values[pos] == 1) || (origin == 1 && values[pos] == 0))
            change.emplace_back(pair<int, int>(start, end));
    }

public:
    SegmentTree(int begin, int end, int *vals) {
        int maxsize = exp2(floor(log2(end - begin) + 1));
        values = new int[maxsize]{0};
        lazy = new int[maxsize]{0};
        length = end - begin;
        size = 0;
        build_tree(0, begin, end, vals);
    }

    vector<pair<int, int>> update_range(int rstart, int rend, int value) {
        change.clear();
        _update_range(0, 0, length, rstart, rend, value);
        print_tree();
        return change;
    }

    void print_tree() {
        queue<int> queue;
        queue.push(0);
        int len = queue.size();
        while (!queue.empty()) {
            auto pos = queue.front();
            queue.pop();
            len--;
            cout << "(" << values[pos] << "," << lazy[pos] << ")" << "  ";
            if ((2 * pos + 1) < size) {
                queue.push(2 * pos + 1);
                queue.push(2 * pos + 2);
            }
            if (len == 0) {
                len = queue.size();
                cout << endl;
            }
        }
    }
};

bool compare(vector<int> a, vector<int> b) {
    if (a[0] == b[0]) {
        if (a[2] == b[2])
            return a[1] < b[1];
        else
            return a[2] < b[2];
    } else
        return a[0] < b[0];
}

class Solution218 {
/*
wjcnote 方法是自己想的，但是效率很不咋地，有待提高；折腾了太长时间了，暂时放一放
**/
public:
    vector<vector<int>> getSkyline(vector<vector<int>> &buildings) {
        if (buildings.size() == 0)
            return (vector<vector<int>>) NULL;
        set<int> s;
        s.insert(0);
        for (auto item : buildings) {
            s.insert(item[2]);
        }
        int index = 0;
        map<int, int> codes;
        int *decodes = new int[s.size()];
        for (auto item : s) {
            codes[item] = index;
            decodes[index] = item;
            index++;
        }
        auto segments = vector<vector<int>>(buildings.size() * 2);
        index = -1;
        for (auto item : buildings) {
            segments[++index] = {item[0], codes[item[2]], 1};
            segments[++index] = {item[1], codes[item[2]], -1};
        }
        sort(segments.begin(), segments.end(), compare);  // wjcnote 这里可以优化
        vector<int> last = segments[0];
        int *arr = new int[codes.size() - 1]{0};
        vector<vector<int>> change;
        for (auto item : segments) {
            auto point = vector<int>{item[0], 0};
            bool flag = false;
            if (last[0] == item[0]) {
                if (last[2] == item[2]) {
                    continue;
                } else {
                    change.pop_back();
                }
            }
            last = item;
            for (int i = 0; i <= item[1] - 1; i++) {
                int current = item[2] == 1 ? i : item[1] - 1 - i;
                int origin = arr[current];
                arr[current] += item[2];
                if ((origin == 0 && arr[current] == 1) || (origin == 1 && arr[current] == 0)) {
                    point[1] = decodes[item[2] == 1 ? current + 1 : current];
                    flag = true;
                }
            }
            if (flag)
                change.push_back(point);
        }
        for (auto point : change)
            cout << "point " << point[0] << " " << point[1] << endl;
    }

    void process() {

    }
};


void test_tree() {
    // wjcnote case1 数据 [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
    vector<vector<int>> case1 = {
//            {2,  9,  10},
//            {3,  7,  15},
//            {5,  12, 12},
//            {15, 20, 10},
//            {19, 24, 8}
            {0, 5, 7},
            {5, 10, 7},
            {5, 10, 12},
            {10, 15, 7},
            {15, 20, 7},
            {15, 20, 12},
            {20, 25, 7}
//            {2, 4, 5},
//            {2, 5, 7}

    };
    // wjcnote 获取y坐标，并离散化
    set<int> s;
    map<int, int> codes;
    s.insert(0);
    for (auto item : case1) {
        s.insert(item[2]);
    }

    int index = 0;
    int *decodes = new int[s.size()];
    for (auto item : s) {
        codes[item] = index;
        decodes[index] = item;
        index++;
    }
    auto segments = vector<vector<int>>(case1.size() * 2);
    index = -1;
    for (auto item : case1) {
        segments[++index] = {item[0], codes[item[2]], 1};
        segments[++index] = {item[1], codes[item[2]], -1};
    }
    sort(segments.begin(), segments.end(), compare);
    for (auto item : segments) {
        cout << item[0] << " " << item[1] <<" "<< item[2] << endl;
    }
    cout <<"排序"<<endl;
    int *arr = new int[codes.size() - 1]{0};
    vector<pair<int, int>> change;
    int last_height = -1;
    for (index = 0; index < segments.size(); index++) {
        auto item = segments[index];
        pair<int, int> point = {item[0], 0};
        bool flag = false;
        for (int i = 0; i <= item[1] - 1; i++) {
            int current = item[2] == 1 ? i : item[1] - 1 - i;
            int origin = arr[current];
            arr[current] += item[2];
            if ((origin == 0 && arr[current] == 1) || (origin == 1 && arr[current] == 0)) {
                point.second = decodes[item[2] == 1 ? current + 1 : current];
                flag = true;
            }
        }
        if (flag) {
            if (change.size() > 0 && point.first == change.back().first) {
                auto last = segments[index - 1];
                if (last[1] == item[1] && last[2] != item[2]) {
                    change.pop_back();
                } else {
                    change.back().second = item[2] == 1 ?
                                           max(point.second, change.back().second) : min(point.second, change.back().second);
                }
            } else
                change.push_back(point);
        }
    }
    for (auto point : change)
        cout << "point " << point.first << " " << point.second << endl;
}


#endif

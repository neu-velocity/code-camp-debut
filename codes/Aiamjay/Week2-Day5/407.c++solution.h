#ifndef _SOLUTION407_H
#define _SOLUTION407_H

#include <iostream>
#include <vector>
#include <queue>
#include "heap.h"

using namespace std;

template<typename E>
class Less {
public:
    static bool prior(E a, E b) {
        return a[2] < b[2];
    }

    static void print(E a) {
        cout << a[0] << " " << a[1] << " " << a[2] << "  ";
    }
};

typedef vector<int> vInt;

class Solution {
    // 这两种方法时间复杂度和空间复杂度都非常高
    // 只是作为一种思路
public:
    int trapRainWater(vector<vInt> &heightMap) {
        int dirs[4][2] = {
                {1,  0},
                {-1, 0},
                {0,  1},
                {0,  -1}
        };
        int width = heightMap[0].size();
        const int height = heightMap.size();
        vector<vector<int>> flags(height, vector<int>(width));
        reset_flags(flags);
        // wjcnote 使用heap
        auto heap = Heap<vector<int>, Less<vector<int>>>(width * 2 + height * 2);
        for (int i = 1; i < width - 1; i++) {
            heap.insert({0, i, heightMap[0][i]});
            heap.insert({height - 1, i, heightMap[height - 1][i]});
            flags[0][i] = flags[height - 1][i] = 1;
        }
        for (int i = 1; i < height - 1; i++) {
            heap.insert({i, 0, heightMap[i][0]});
            heap.insert({i, width - 1, heightMap[i][width - 1]});
            flags[i][0] = flags[i][width - 1] = 1;
        }
        print_2d_vector(flags);
        heap.print_heap();
        cout << endl;
        int result = 0;
        while (!heap.empty()) {
            auto top = heap.remove_first();
            for (auto item : dirs) {
                int i = top[0] + item[0];
                int j = top[1] + item[1];
                if (i >= height or i < 0 or j >= width or j < 0 or flags[i][j] == 1)
                    continue;
                if ((i == 0 || i == height - 1) && (j == 0 || j == width - 1))
                    continue;
                result += max(0, top[2] - heightMap[i][j]);
                if (top[2] - heightMap[i][j] > 0)
                    cout << "从" << i << " " << j << " 采集：" << top[2] - heightMap[i][j] << endl;
                heap.insert({i, j, max(top[2], heightMap[i][j])});
                flags[i][j] = 1;
                heap.print_heap();
                cout << endl;
            }
        }
        return result;
    }

    int trapRainWater2(vector<vector<int>> &heightMap) {
        int dirs[4][2] = {
                {1,  0},
                {-1, 0},
                {0,  1},
                {0,  -1}
        };
        int height = heightMap.size();
        int width = height == 0 ? 0 : heightMap[0].size();
        vector<vInt> flags(height, vInt(width));
        if (width != 0)
            reset_flags(flags);
        priority_queue<vInt, vector<vInt>, function<bool(vInt, vInt)>> heap(lesser);
        for (int i = 1; i < width - 1; i++) {
            heap.push({0, i, heightMap[0][i]});
            heap.push({height - 1, i, heightMap[height - 1][i]});
            flags[0][i] = flags[height - 1][i] = 1;
        }
        for (int i = 1; i < height - 1; i++) {
            heap.push({i, 0, heightMap[i][0]});
            heap.push({i, width - 1, heightMap[i][width - 1]});
            flags[i][0] = flags[i][width - 1] = 1;
        }
        int result = 0;
        while (!heap.empty()) {
            auto top = heap.top();
            heap.pop();
            for (auto item : dirs) {
                int i = top[0] + item[0];
                int j = top[1] + item[1];
                if (i >= height or i < 0 or j >= width or j < 0 or flags[i][j] == 1)
                    continue;
                if ((i == 0 || i == height - 1) && (j == 0 || j == width - 1))
                    continue;
                result += max(0, top[2] - heightMap[i][j]);
                if (top[2] - heightMap[i][j] > 0)
                    cout << "从" << i << " " << j << " 采集：" << top[2] - heightMap[i][j] << endl;
                heap.push({i, j, max(top[2], heightMap[i][j])});
                flags[i][j] = 1;
            }
        }
        return result;
    }

    static bool lesser(vInt a, vInt b) {
        return a[2] > b[2];
    }

    static void reset_flags(vector<vector<int>> &data) {
        int height = data.size();
        int width = data[0].size();
        for (auto item : data) {
            fill(item.begin(), item.end(), 0);
        }
    }

    static void print_2d_vector(vector<vector<int>> data) {
        int height = data.size();
        int width = data[0].size();
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                cout << data[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
};

void test_solution() {
    auto s = Solution();
    auto heightMap = vector<vector<int>>{
            {1, 4, 3, 1, 3, 2},
            {3, 2, 1, 3, 2, 4},
            {2, 3, 3, 2, 3, 1}
    };
    cout << s.trapRainWater2(heightMap) << endl;
}

#endif //_SOLUTION407_H

//
// Created by 长夜总有天亮时 on 2019-06-17.
//
#ifndef __HEAP__
#define __HEAP__

#include <iostream>
#include <assert.h>
#include <queue>
#include <vector>
#include <map>

using namespace std;

template<typename E>
class Larger {
public:
    static bool prior(E a, E b) {
        return a > b;
    }
};

template<typename E>
class Smaller {
public:
    static bool prior(E a, E b) {
        return a < b;
    }
};

template<typename E, typename Comp>
class Heap {
    /* wjcnote 数组实现的堆
     * */
private:
    E *heap;  // wjcnote 数组，存储数据
    int maxsize;
    int n;  // wjcnote 堆中数据个数

    void siftdown(int pos) {
        while (!is_leaf(pos)) {
            int j = left_child(pos);
            int rc = right_child(pos);
            if ((rc < n) && (Comp::prior(heap[rc], heap[j])))
                // wjcnote 最大堆，则heap[rc] > heap[j]，j始终指向两个child中大的那个
                j = rc;
            if (Comp::prior(heap[pos], heap[j]))
                // wjcnote 最大堆，把当前子树(pos, left ,right)中元素最大的找出来，如果pos处已经是最大的，说明最大堆没有问题
                return;
            swap(heap, pos, j);
            // wjcnote 如果pos处不是最大值，则将left/right中最大的与pos处交换，
            // wjcnote 交换完成之后，改动的那个子树，可能还存在问题，继续迭代
            pos = j;
        }
    }

    void siftup(int pos) {
        while ((pos != 0) && (Comp::prior(heap[pos], heap[parent(pos)]))) {
            swap(heap, pos, parent(pos));
            pos = parent(pos);
        }
    }

    void swap(E *arr, int index_a, int index_b) {
        E temp = arr[index_a];
        arr[index_a] = arr[index_b];
        arr[index_b] = temp;
    }

public:

    Heap(int max) : maxsize(max) {
        heap = new int[max];
        n = 0;
    }

    Heap(E *h, int num, int max) {
        heap = h;
        n = num;
        maxsize = max;
        build_heap();
    }

    bool is_leaf(int pos) {
        return (pos >= n / 2) && (pos < n);
    }

    int left_child(int pos) {
        return 2 * pos + 1;
    }

    int right_child(int pos) {
        return 2 * pos + 2;
    }

    int parent(int pos) {
        return (pos - 1) / 2;
    }

    void build_heap() {
        // question 这里直接从 n / 2 - 1 开始？？？
        // wjcnote 最后一个元素的parent是 (n - 1 - 1) / 2 ，然后从最后一个元素开始siftdown，
        for (int i = n / 2 - 1; i >= 0; i--) {
            siftdown(i);
        }
    }

    const int size() {
        return n;
    }

    E top() {
        assert(n >= 1);
        return heap[0];
    }

    const E *get_content() {
        return heap;
    }

    void insert(const E &it) {
        assert(n < maxsize);
        int curr = n++; //wjcnote 放置在最后位置
        heap[curr] = it;
        // wjcnote 调整 Heap的结构
//        while ((curr != 0) && (Comp::prior(heap[curr], heap[parent(curr)]))) {
//            // wjcnote 如果是最大堆，判断条件是 curr != 0 && heap[curr] > heap[parent(curr)]
//            swap(heap, curr, parent(curr));
//            curr = parent(curr);
//        }
        siftup(curr);
    }

    bool empty() {
        return n == 0;
    }

    E remove_first() {
        assert(n > 0);
        swap(heap, 0, --n); // wjcnote 将第一个元素与最后一个元素交换
        if (n != 0)
            siftdown(0);
        return heap[n];
    }

    E remove(int pos) {
        assert(pos < n);
        // wjcnote 最后一个元素，啥也不需要做
        if (pos == (n - 1))
            n--;
        else {
            // wjcnote 将当前需要删除的与最后一个元素交换
            swap(heap, pos, --n);
//            while ((pos != 0) && (Comp::prior(heap[pos], heap[parent(pos)]))) {
//                swap(heap, parent(pos), pos);
//                pos = parent(pos);
//            }
            siftup(pos);
            // wjcnote 这里是n != 0， 不是pos
            // question 这里要么向上，要么向下，不可能两个都要执行
            // wjcnote 在siftdown这个函数里面，如果发现pos大于left和right，直接返回，不会有后面的操作了
            // wjcnote 这里解释了为什么这边siftup之后siftdown
            if (n != 0)
                siftdown(pos);
        }
        return heap[n];
    }

    void print_heap() {
        if (n == 0)
            return;
        queue<int> s;
        s.push(0);
        int len = s.size();
        while (!s.empty()) {
            int pos = s.front();
            s.pop();
            len--;
            cout << heap[pos] << "  ";
            if (!is_leaf(pos)) {
                if (left_child(pos) < n)
                    s.push(left_child(pos));
                if (right_child(pos) < n)
                    s.push(right_child(pos));
            }
            if (len == 0) {
                cout << endl;
                len = s.size();
            }
        }
    }
};

void test_heap_inner() {
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    auto heap = new Heap<int, Smaller<int>>(a, 7, 10);
    for (int i = 0; i < heap->size(); i++) {
        cout << heap->get_content()[i] << " ";
    }
    cout << endl;
    heap->print_heap();
}

class MedianFinder {
private:
    priority_queue<int, vector<int>, less<>> lower;
    priority_queue<int, vector<int>, greater<>> upper;
public:
    /** initialize your data structure here. */
    MedianFinder() {
    }

    void addNum(int num) {
        if (lower.empty()) {
            lower.push(num);
            return;
        }
        auto a = lower.top();
        int b = -1;
        if (!upper.empty())
            b = upper.top();
        if (num < lower.top()) {
            lower.push(num);
            if (lower.size() - upper.size() > 1) {
                auto top = lower.top();
                lower.pop();
                upper.push(top);
            }
        } else {
            upper.push(num);
            if (upper.size() > lower.size()) {
                auto top = upper.top();
                upper.pop();
                lower.push(top);
            }
        }
    }

    double findMedian() {
        auto len = lower.size() + upper.size();
        if (len % 2 == 0) {
            return (lower.top() + upper.top()) / 2.;
        } else {
            auto a = lower.top();
            return a;
        }
    }
};

class MedianFinder2 {
private:
    Heap<int, Smaller<int>> upper;
    Heap<int, Larger<int>> lower;
public:
    MedianFinder2() : upper(100), lower(100) {
    }

    void addNum(int num) {
        if (lower.empty()) {
            lower.insert(num);
            return;
        }
        if (num < lower.top()) {
            lower.insert(num);
            if (lower.size() - upper.size() > 1) {
                auto top = lower.remove_first();
                upper.insert(top);
            }
        } else {
            upper.insert(num);
            if (upper.size() > lower.size()) {
                auto top = upper.remove_first();
                lower.insert(top);
            }
        }
    }

    double findMedian() {
        auto len = lower.size() + upper.size();
        if (len % 2 == 0) {
            return (lower.top() + upper.top()) / 2.;
        } else {
            auto a = lower.top();
            return a;
        }
    }
};

void test_solution() {
    vector<int> input = {40, 12, 16, 14, 35, 19, 34, 35, 28, 35, 26, 6, 8, 2, 14, 25, 25, 4, 33, 18, 10, 14, 27, 3, 35,
                         13, 24, 27, 14, 5, 0, 38, 19, 25, 11, 14, 31, 30, 11, 31, 0};
    vector<float> output = {40.0, 26.0, 16.0, 15.0, 16.0, 17.5, 19.0, 26.5, 28.0, 31.0, 28.0, 27.0, 26.0, 22.5, 19.0,
                            22.0, 25.0, 22.0, 25.0, 22.0, 19.0, 18.5, 19.0, 18.5, 19.0, 18.5, 19.0, 21.5, 19.0, 18.5,
                            18.0, 18.5, 19.0, 19.0, 19.0, 18.5, 19.0, 19.0, 19.0, 19.0, 19.0};
    auto median = new MedianFinder2();
    vector<float> result;
    for (auto item : input) {
        median->addNum(item);
        auto a = median->findMedian();
        result.push_back(a);
    }
    for (int i = 0; i < output.size(); i++) {
        assert(result[i] == output[i]);
    }
}

#endif
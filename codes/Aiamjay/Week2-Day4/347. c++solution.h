#ifndef __SOLUTION__
#define __SOLUTION__

#include <vector>
#include <map>
#include <iostream>

template<typename E, typename F>
class Pair_Minor {
public:
    static bool prior(const pair<E, F> one, const pair<E, F> two) {
        return one.second < two.second;
    }
};

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
    E *heap;
    int maxsize;
    int n;

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
        for (int i = n / 2 - 1; i >= 0; i--) {
            siftdown(i);
        }
    }

    const int get_size() {
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

class Solution {
public:
    vector<int> topKFrequent(vector<int> &nums, int k) {
        //wjcnote 首先，统计，然后再使用heap，最小堆就行了
        map<int, int> dict;
        for (int item : nums) {
            auto temp = dict.find(item);
            if (temp == dict.end())
                dict.insert({item, 1});
            else
                temp->second += 1;
        }
        auto temp = new pair<int, int>[k];
        // copy first k element into heap
        auto iter = dict.begin();
        for (int i = 0; i < k; i++, iter++) {
            temp[i] = {iter->first, iter->second};
        }
        auto heap = new Heap<pair<int, int>, Pair_Minor<int, int>>(temp, k, dict.size());

        for (; iter != dict.end(); iter++) {
            if (Pair_Minor<int, int>::prior(heap->top(), {iter->first, iter->second})) {
                // 如果heap头元素要小于dict中的当前元素，则heap中移除头元素，加入当前
                heap->remove_first();
                heap->insert({iter->first, iter->second});
            }
        }
        // wjcnote 得到最终的结果。转换成vector, 这里简单粗暴一点，直接拿到heap的数组
        auto result = vector<int>(heap->get_size());
        for (int i = 0; i < heap->get_size(); i++) {
            result[i] = heap->get_content()[i].first;
        }
        for (int i = 0; i < heap->get_size(); i++) {
            cout << "值：" << heap->get_content()[i].first << " " << "出现: " << heap->get_content()[i].second << "次"
                 << endl;
        }
        return result;
    }

    void test() {
        vector<int> a = {1, 1, 1, 2, 2, 3};
        auto s = new Solution();
        auto result = s->topKFrequent(a, 2);
    }
};

// wjcnote 遍历 map 的三种方式
//    for (auto iter = a.begin(); iter != a.end(); iter++) {
//        cout << iter->first << "  " << iter->second << endl;
//    }
//    for (auto x : a) {
//        cout << x.first << "  " << x.second << endl;
//    }
//    for (auto&&[first, second] : a) {
//        cout << first << "  " << second << endl;
//    }
#endif
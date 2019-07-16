import math


class Heap:
    def __init__(self, op, data):
        """
        :param op: 排序函数
        """
        self.op = op
        self.data = data
        self.__build_heap__()

    def __sift_down__(self, pos):
        while not self.is_leaf(pos):
            target = self.left(pos)
            right = self.right(pos)
            if right < self.length and self.op(self.data[right], self.data[target]):
                target = right
            if self.op(self.data[pos], self.data[target]):
                return
            self.data[pos], self.data[target] = self.data[target], self.data[pos]
            pos = target

    def __sift_up__(self, pos):
        parent = self.parent(pos)
        while pos > 0 and self.op(self.data[pos], self.data[parent]):
            self.data[pos], self.data[parent] = self.data[parent], self.data[pos]
            pos = parent
            parent = self.parent(pos)

    def __build_heap__(self):
        for i in range(int(self.length / 2 - 1), -1, -1):
            self.__sift_down__(i)

    @property
    def top(self):
        assert self.length >= 1
        return self.data[0]

    def insert(self, item):
        # wjcnote 放置在最后
        self.data.append(item)
        # siftup
        self.__sift_up__(self.length - 1)

    def remove_top(self):
        if self.length == 1:
            return self.data.pop()
        elif self.length == 2:
            result = self.data[0]
            self.data = self.data[1:]
            return result
        else:
            # wjcnote 把最后一个元素与top元素交换
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            result = self.data.pop()
            self.__sift_down__(0)
            return result

    def remove_index(self, index):
        """remove element at specific index"""
        # wjcnote 与最后一个元素交换
        assert index < self.length
        if index == self.length - 1:
            return self.data.pop()
        else:
            self.data[index], self.data[-1] = self.data[-1], self.data[index]
            result = self.data.pop()
            # wjcnote 先向上，要么向上，要么向下
            if self.op(self.data[index], self.data[self.parent(index)]):
                self.__sift_up__(index)
            else:
                self.__sift_down__(index)
            return result

    def print_heap(self):
        max_height = math.floor(math.log2(self.length))
        index = 0
        for i in range(max_height):
            print(" ".join([str(item) for item in self.data[index: 2 ** i + index]]))
            index += 2 ** i
        print(" ".join([str(item) for item in self.data[index:]]))

    @property
    def length(self):
        return len(self.data)

    @staticmethod
    def left(pos):
        return pos * 2 + 1

    @staticmethod
    def right(pos):
        return pos * 2 + 2

    @staticmethod
    def parent(pos):
        return int((pos - 1) / 2)

    def is_leaf(self, pos):
        return int(self.length / 2) <= pos < self.length


class MedianFinder:
    def __init__(self):
        """initialize your data structure here."""
        self.upper = Heap(lambda a, b: a > b, [], 0)
        self.lower = Heap(lambda a, b: a < b, [], 0)
        pass

    def addNum(self, num: int) -> None:
        # wjcnote 控制在lower.length - upper.length <= 1
        if self.lower.top >= num:
            self.lower.insert(num)
        else:
            self.upper.insert(num)
        if self.upper.length - self.lower.length == 1:
            self.lower.insert(self.upper.remove_top())
        if self.lower.length - self.upper.length > 1:
            self.upper.insert(self.upper.remove_top())

    def findMedian(self) -> float:
        if (self.upper.length + self.lower.length) % 2 == 0:
            return (self.lower.top + self.upper.top) / 2
        else:
            return self.lower.top


def test_fun():
    data = [2, 4, 1, 3, 5, 8, 9]
    heap = Heap(lambda a, b: a > b, data)
    # heap.print_heap()
    # print("insert value with 10 ")
    heap.insert(10)
    # heap.print_heap()
    print("remove top ", heap.remove_top())
    heap.print_heap()
    print("insert value with 7 ")
    heap.insert(7)
    heap.print_heap()
    print("insert value with 11 ")
    heap.insert(11)
    heap.print_heap()
    heap.remove_index(3)
    print("remove element in index = 3 ")
    heap.print_heap()
    heap.remove_index(4)
    print("remove element in index = 4 ")
    heap.print_heap()

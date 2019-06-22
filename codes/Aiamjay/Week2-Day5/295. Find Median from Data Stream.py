from codes.Aiamjay.utils.heap import Heap


class MedianFinder:

    def __init__(self):
        self.upper = Heap(lambda a, b: a < b, [])
        self.lower = Heap(lambda a, b: a > b, [])

    def addNum(self, num):
        if self.lower.length == 0:
            self.lower.insert(num)
            return
        if num < self.lower.top:
            self.lower.insert(num)
            if self.lower.length - self.upper.length > 1:
                self.upper.insert(self.lower.remove_top())
        else:
            self.upper.insert(num)
            if self.upper.length > self.lower.length:
                self.lower.insert(self.upper.remove_top())

    def findMedian(self):
        if (self.lower.length + self.upper.length) % 2 == 0:
            return (self.lower.top + self.upper.top) / 2
        else:
            return self.lower.top


def test_solution_295():
    data = [40, 12, 16, 14, 35, 19, 34, 35, 28, 35, 26, 6, 8, 2, 14, 25, 25, 4, 33, 18, 10, 14, 27, 3,
            35, 13, 24, 27, 14, 5, 0, 38, 19, 25, 11, 14, 31, 30, 11, 31, 0]
    output = [40.0, 26.0, 16.0, 15.0, 16.0, 17.5, 19.0, 26.5, 28.0, 31.0, 28.0, 27.0, 26.0, 22.5, 19.0,
              22.0, 25.0, 22.0, 25.0, 22.0, 19.0, 18.5, 19.0, 18.5, 19.0, 18.5, 19.0, 21.5, 19.0, 18.5,
              18.0, 18.5, 19.0, 19.0, 19.0, 18.5, 19.0, 19.0, 19.0, 19.0, 19.0]
    median = MedianFinder()
    result = []
    for item in data:
        median.addNum(item)
        result.append(median.findMedian())
    assert result == output


if __name__ == '__main__':
    test_solution_295()

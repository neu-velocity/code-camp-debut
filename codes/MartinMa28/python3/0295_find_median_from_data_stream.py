class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        
    def _binary_search(self, num: int, lower: int, upper: int) -> int:
        """
        num: the number you want to insert into the array
        lower: lower bound of current recursion (inclusive)
        upper: upper bound of current recursion (exclusive)
        return value: the index of the proper place for your insertion
        """
        if len(self.heap[lower: upper]) <= 1:
            if num <= self.heap[lower]:
                return lower
            else:
                return lower + 1

        mid = (lower + upper) // 2

        if num == self.heap[mid]:
            return mid
        elif num < self.heap[mid]:
            return self._binary_search(num, lower, mid)
        else:
            return self._binary_search(num, mid, upper)

    def addNum(self, num: int) -> None:
        if self.heap == []:
            self.heap.append(num)
        elif len(self.heap) == 1:
            if num <= self.heap[0]:
                self.heap.insert(0, num)
            else:
                self.heap.insert(1, num)
        else:
            ind = self._binary_search(num, 0, len(self.heap))
            self.heap.insert(ind, num)

    def findMedian(self) -> float:
        if len(self.heap) % 2 == 1:
            return self.heap[len(self.heap) // 2]
        else:
            return float(self.heap[len(self.heap) // 2 - 1] + self.heap[len(self.heap) // 2]) / 2


if __name__ == "__main__":
    solu = MedianFinder()

    solu.addNum(1)
    solu.addNum(2)
    solu.addNum(3)

    print(solu.heap)
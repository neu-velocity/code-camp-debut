# encoding=utf-8
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def worker(begin, end):
            if begin == end:
                return begin if self.isBadVersion(begin) else n + 1
            mid = int((begin + end) / 2)
            if self.isBadVersion(mid):
                return min(mid, worker(begin, max(0, mid - 1)))
            else:
                return worker(min(mid + 1, end), end)

        return worker(1, n)

    def isBadVersion(self, pos):
        self.count += 1
        return self.version_dict[pos]

    def test_solution(self):
        # case 1
        self.version_dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        self.count = 0
        assert self.firstBadVersion(len(self.version_dict)) == 7
        print("count ", self.count, " times")
        # case 2
        self.count = 0
        self.version_dict[5] = 1
        self.version_dict[6] = 1
        assert self.firstBadVersion(len(self.version_dict)) == 5
        print("count ", self.count, " times")
        # case 3
        self.count = 0
        self.version_dict[4] = 1
        assert self.firstBadVersion(len(self.version_dict)) == 4
        print("count ", self.count, " times")
        # case 4
        self.count = 0
        self.version_dict = {
            1: 1,
            2: 1,
            3: 1,
        }
        assert self.firstBadVersion(len(self.version_dict)) == 4
        print("count ", self.count, " times")


if __name__ == '__main__':
    s = Solution()
    s.test_solution()

# encoding=utf-8


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # wjcnote 用python的dict和sort函数,纯属投机曲奇
        dicts = {}
        for item in nums:
            if item not in dict:
                dicts[item] = 1
            else:
                dicts[item] += 1
        result = sorted(dicts, key=lambda x: x[1])
        return [item[0] for item in result[:k]]


if __name__ == '__main__':
    s = Solution()

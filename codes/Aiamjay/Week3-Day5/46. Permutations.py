from collections import (
    defaultdict, deque
)


class Solution1:
    def __init__(self):
        self.graph = None

    def permute(self, nums):
        # 构造图
        self.build_graph(nums)
        result = []
        for num in nums:
            result += self.bfs(num)
        return result

    def build_graph(self, nums):
        length = len(nums)
        self.graph = defaultdict(list)
        for i in range(length):
            for j in range(i + 1, length):
                self.graph[nums[i]].append(nums[j])
                self.graph[nums[j]].append(nums[i])

    def bfs(self, node):
        queue = deque()
        queue.append([node])
        result = []
        while queue:
            path = queue.popleft()
            cur_node = path[-1]
            flag = False
            for neighbor in self.graph[cur_node]:
                if neighbor not in path:
                    flag = True
                    queue.append(path + [neighbor])
            if not flag:
                result.append(path)
        return result

    def test_solution(self):
        # case 1
        nums = [1, 2, 3]
        print(self.permute(nums))

        # case 2
        nums = [1, 2, 3, 4, 5]
        result = self.permute(nums)
        print(len(result))
        for item in result:
            print(item)


class Solution2:
    def __init__(self):
        pass

    def permute(self, nums):
        result = []
        self.worker(nums, [], result)
        return result

    def worker(self, nums, path, result):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            self.worker(nums[:i] + nums[i + 1:], path + [nums[i]], result)

    def test_solution(self):
        # case 1
        nums = [1, 2, 3]
        print(self.permute(nums))

        # case 2
        nums = [1, 2, 3, 4, 5]
        result = self.permute(nums)
        print(len(result))
        for item in result:
            print(item)


if __name__ == '__main__':
    s = Solution2()
    s.test_solution()
    pass

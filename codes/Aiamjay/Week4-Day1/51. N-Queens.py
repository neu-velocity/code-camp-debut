# encoding = utf-8


class Solution1:
    def solveNQueens(self, n: int):
        temp_result = []
        result = []
        self.NUMS = set(list(range(n)))
        self.dfs(n, [], temp_result)
        for item in temp_result:
            temp = []
            print(item)
            for index in item:
                line = '.' * index + 'Q' + '.' * (n - index - 1)
                temp.append(line)
            result.append(temp)
        return result

    def dfs(self, n, path, result: list):
        if len(path) == n:
            result.append(path)
            return
        nodes = self.bounding_condition(n, path)
        for node in nodes:
            self.dfs(n, path + [node], result)

    def bounding_condition(self, n, prev_nodes: list):
        # wjcnote bounding condition for the dfs
        # wjcnote 检查是否是处于对角线
        cur_step = len(prev_nodes)
        result = set(prev_nodes)
        for index in range(len(prev_nodes)):
            if prev_nodes[index] - (cur_step - index) >= 0:
                result.add(prev_nodes[index] - (cur_step - index))
            if prev_nodes[index] + (cur_step - index) < n:
                result.add(prev_nodes[index] + (cur_step - index))
        return self.NUMS.difference(result)

    def test_solution(self):
        n = 4
        result = self.solveNQueens(n)
        print("一共有： ", len(result))
        for item in result:
            print(item)


if __name__ == '__main__':
    s = Solution1()
    s.test_solution()

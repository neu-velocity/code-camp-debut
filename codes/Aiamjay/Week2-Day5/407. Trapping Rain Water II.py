from codes.Aiamjay.utils.heap import Heap


class Solution:

    def trapRainWater(self, heightMap):
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        height = len(heightMap)
        width = len(heightMap[0]) if height else 0
        flags = [[0 * width] * height]
        # wjcnote 使用heap
        heap = Heap([], lambda a, b: a[2] < b[2])
        for i in range(1, width):
            heap.insert([0, i, heightMap[0][i]])
            heap.insert([height - 1, i, heightMap[height - 1][i]])
            flags[0][i] = flags[height - 1][i] = 1
        for i in range(1, height):
            heap.insert([i, 0, heightMap[i][0]])
            heap.insert([i, width - 1, heightMap[i][width - 1]])
            flags[i][0] = flags[i][width - 1] = 1
        result = 0
        while heap.length:
            top = heap.remove_top()
            for item in dirs:
                i = top[0] + item[0]
                j = top[1] + item[1]
                if i >= height or i < 0 \
                        or j >= width or j < 0 \
                        or flags[i][j] == 1 \
                        or ((i == 0 or i == height - 1) and (j == 0 or j == width - 1)):
                    continue
                result += max(0, top[2] - heightMap[i][j])
                if top[2] - heightMap[i][j] > 0:
                    print("从", i, " ", j, " 采集：", top[2] - heightMap[i][j])
                heap.insert([i, j, max(top[2], heightMap[i][j])])
                flags[i][j] = 1
                heap.print_heap()
        return result

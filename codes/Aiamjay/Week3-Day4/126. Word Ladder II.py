# encoding = utf-8
from collections import (
    defaultdict, deque
)
from math import inf


class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list):
        if endWord not in wordList or not wordList:
            return 0
        # # wjcnote 创建图
        word_dict = defaultdict(list)
        word_len = len(beginWord)
        for word in wordList:
            for i in range(word_len):
                word_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # wjcnote 搜索图 bfs
        queue = deque([(beginWord, 1)])
        visited = set()
        graph = defaultdict(set)
        distances = dict()
        min_len = inf
        while queue:
            cur, length = queue.popleft()
            for i in range(word_len):
                key = cur[:i] + '*' + cur[i + 1:]
                for word in word_dict[key]:
                    if word != cur and word not in graph[cur]:
                        graph[word].add(cur)
                        distances[word] = min(distances[word], length) if word in distances else length
                    if word not in visited:
                        if word == endWord:
                            min_len = min(min_len, length + 1)
                        visited.add(word)
                        queue.append((word, length + 1))

        # for item in graph:
        #     print(item, " ", graph[item])
        #
        # for item in distances:
        #     print(item, " ", distances[item])

        return self.find_all_path(distances, graph, endWord, beginWord, min_len - 1)

    def find_all_path(self, distances, graph, node, end, length):
        if length == 1:
            return [[end, node]]
        result = []
        for parent in graph[node]:
            if distances[parent] == length - 1:
                result += [item + [node] for item in self.find_all_path(distances, graph, parent, end, length - 1)]
        return result

    def test_solution(self):
        # case 1
        # begin_word = "hit"
        # end_word = "cog"
        # word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        # result = self.ladderLength(begin_word, end_word, word_list)
        # print(result)
        # assert sorted(result) == sorted(
        #        [
        #            ["hit", "hot", "lot", "log", "cog"],
        #            ["hit", "hot", "dot", "dog", "cog"],
        #        ])

        # case 2
        begin_word = "red"
        end_word = "tax"
        word_list = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
        print(self.ladderLength(begin_word, end_word, word_list))
        assert sorted(self.ladderLength(begin_word, end_word, word_list)) == sorted(
            [["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]]
        )


if __name__ == '__main__':
    s = Solution1()
    s.test_solution()

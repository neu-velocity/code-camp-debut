# encoding = utf-8
from collections import (
    defaultdict, deque
)


class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
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
        while queue:
            cur, length = queue.popleft()
            # wjcnote 尽量少的使用 in
            # wjcnote 使用 in 尽量少使用 list， 优先使用set
            for i in range(word_len):
                key = cur[:i] + '*' + cur[i + 1:]
                if key not in visited:
                    visited.add(key)
                    for word in word_dict[key]:
                        if word == endWord:
                            return length + 1
                        if word not in visited:
                            visited.add(word)
                            queue.append((word, length + 1))

        return 0

    def test_solution(self):
        # case 1
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        print(self.ladderLength(begin_word, end_word, word_list))

        # case 2
        begin_word = "hot"
        end_word = "dog"
        word_list = ["hot", "dog"]
        print(self.ladderLength(begin_word, end_word, word_list))


class Solution2:

    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        if not wordList or endWord not in wordList:
            return 0
        # wjcnote create graph
        word_len = len(beginWord)
        word_graph = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                word_graph[word[:i] + '_' + word[i + 1:]].append(word)
        forward = deque([(beginWord, 1)])
        backward = deque([(endWord, 1)])
        forward_visited = {beginWord: 1}
        backward_visited = {endWord: 1}
        while forward and backward:
            # wjcnote search forward
            ans = self.search(forward, forward_visited, backward_visited, word_graph)
            if ans:
                return ans
            # wjcnote search backward
            ans = self.search(backward, backward_visited, forward_visited, word_graph)
            if ans:
                return ans
        return 0

    def search(self, queue: deque, visited: set, other_visited: set, graph: defaultdict):
        top_word, cur_len = queue.popleft()
        for i in range(len(top_word)):
            for word in graph[top_word[:i] + '_' + top_word[i + 1:]]:
                if word in other_visited:
                    return cur_len + other_visited[word]
                if word not in visited:
                    visited[word] = cur_len + 1
                    queue.append((word, cur_len + 1))
        return None

    def test_solution(self):
        # case 1
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        print(self.ladderLength(begin_word, end_word, word_list))

        # case 2
        begin_word = "hot"
        end_word = "dog"
        word_list = ["hot", "dog"]
        print(self.ladderLength(begin_word, end_word, word_list))


if __name__ == '__main__':
    s = Solution1()
    s.test_solution()

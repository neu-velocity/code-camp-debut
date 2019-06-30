class Solution:
    def _replacement(self, word: str) -> list:
        reps = []
        for l_i, l in enumerate(word):
            reps.append(word[:l_i] + '*' + word[l_i + 1:])

        return reps

    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        if wordList == []:
            return 0
        
        reps_to_words = {}

        for w in wordList:
            reps = self._replacement(w)
            for rep in reps:
                reps_to_words[rep] = reps_to_words.get(rep, []) + [w]

        
        word_queue = []
        visited = []
        word_queue.append((beginWord, 1))

        while len(word_queue) > 0:
            current_word, current_level = word_queue.pop(0)
            current_reps = self._replacement(current_word)

            for rep in current_reps:
                next_words = reps_to_words.get(rep, [])
                for w in next_words:
                    if w not in visited:
                        if w != endWord:
                            visited.append(w)
                            word_queue.append((w, current_level + 1))
                        else:
                            # reach the endWord
                            return current_level + 1

        return 0


if __name__ == "__main__":
    solu = Solution()
    print(solu.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
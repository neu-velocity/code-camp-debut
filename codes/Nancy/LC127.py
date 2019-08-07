class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(wordList) == 0 or endWord not in wordList:
            return 0
        
        #preprocess wordList, save all intermediate states in a dictionary
        N = len(beginWord)
        d = {}
        for word in wordList:
            for i in range(N):
                tmp = word[:i] + '*' + word[i + 1:]
                if tmp not in d:
                    d[tmp] = [word]
                else:
                    d[tmp].append(word)
        
        queue = [(beginWord, 1)]
        
        visited = [beginWord]
        while len(queue) != 0:
            current_word, level = queue.pop(0)
            for i in range(N):
                #intermediate form of current word
                nextWord_combo = current_word[:i] + '*' + current_word[i + 1:]
                
                if nextWord_combo in d:
                    for nextword in d[nextWord_combo]:
                        #if we meet the endWord, found the shortest path and return!
                        if nextword == endWord:
                            return level + 1
                       
                        #prevent cycles, we don't want to revisited the word has been visited in the current path                    
                        if nextword not in visited:
                            visited.append(nextword)
                            queue.append((nextword, level + 1))
        return 0
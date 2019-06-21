/*
 * @lc app=leetcode id=127 lang=cpp
 *
 * [127] Word Ladder
 */
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> mySet(wordList.begin(), wordList.end()), head, tail, *phead, *ptail;
        if(mySet.find(endWord) == mySet.end())
            return 0;
        head.insert(beginWord);
        tail.insert(endWord);
        int len = 2;
        while(!head.empty() && !tail.empty()) {
            if(head.size() < tail.size()) {
                phead = &head;
                ptail = &tail;
            }else{
                phead = &tail;
                ptail = &head;
            }
            unordered_set<string> tmp;
            for(auto it = phead->begin(); it != phead->end(); it++) {
                string word = *it;
                for(int i = 0; i < word.length(); i++) {
                    char t = word[i];
                    for(int j = 0; j < 26; j++) {
                        word[i] = 'a' + j;
                        if(ptail->find(word) != ptail->end()) {
                            return len;
                        }
                        if(mySet.find(word) != mySet.end()) {
                            mySet.erase(word);
                            tmp.insert(word);
                        }
                    }
                    word[i] = t;
                }
            } 
            len++;
            phead->swap(tmp);
        }
        return 0;
       
    }
};


class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> mySet(wordList.begin(), wordList.end());
        vector<vector<string>> ret;
        unordered_map<string, vector<string>> hash;
        unordered_map<string, int> distance;
        if(mySet.find(endWord) == mySet.end())
            return ret;
        queue<string> q;
        q.push(beginWord);
        distance[beginWord] = 0;
        bool find = false;
        while(!q.empty() && !find) {
            int size = q.size();
            for(int i = 0; i < size; i++) {
                vector<string> tmp;
                string word = q.front();
                if(word == endWord) {
                    find = true;
                    break;
                }
                q.pop();
                string origin = word;
                for(int i = 0; i < word.length(); i++) {
                    char t = word[i];
                    for(int j = 0; j <= 26; j++) {
                        word[i] = 'a' + j;
                        if(word[i] == t)
                            continue;
                        if(mySet.find(word) != mySet.end()) {
                            tmp.push_back(word);
                            if(distance.find(word) == distance.end()) {
                                q.push(word);
                                distance[word] = distance[origin] + 1;    
                            }
                        }
                    }
                    word[i] = t;
                }
                hash[word] = tmp;
            }
        }
        if(!find)
            return ret;
        vector<string> current = {beginWord};
        dfs(ret, current, endWord, hash, distance);
        return ret;
    }
    
    void dfs(vector<vector<string>>& ret, 
             vector<string>& current, 
             string endWord, 
             unordered_map<string, vector<string>>& hash,
             unordered_map<string, int>& distance) {
        string last = current[current.size()-1];
        if(last == endWord) {
            ret.push_back(current);
            return;
        }
        vector<string> nextLevel = hash[last];
        for(string nextString: nextLevel) {
            if(distance[nextString] == distance[last] + 1) {
                current.push_back(nextString);
                dfs(ret, current, endWord, hash, distance);
                current.pop_back();   
            }
        }
    }
};


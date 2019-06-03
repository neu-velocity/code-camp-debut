class Solution {
public:
    string decodeString(string s) {
        if(s.length() == 0)
            return s;
        stack<string> st;
        int i = 0;
        while(i < s.length()) {
            if(s[i] >= '0' && s[i] <= '9') {
                int k = i+1;
                while(s[k] >= '0' && s[k] <= '9') {
                    k++;
                }
                st.push(s.substr(i, k - i));
                i = k;
            } else if(s[i] == ']') {
                string tmp = "";
                string result = "";
                while(st.top() != "[") {
                    tmp.insert(tmp.length(), st.top());
                    st.pop();
                }
                st.pop();
                string topNumber = st.top();
                int time = stoi(topNumber);
                st.pop();
                for(int i = 0; i < time; i++) {
                    result += tmp;
                }
                st.push(result);
                i++;
            }else {
                st.push(string(1, s[i]));
                i++;
            }
        }
        string ret = "";
        while(!st.empty()) {
            ret.insert(ret.length(), st.top());
            st.pop();
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
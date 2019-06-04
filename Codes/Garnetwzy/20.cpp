class Solution {
public:
   bool isValid(string s) {
    stack<char> st;
    char p;
    for(int i=0;s[i]!='\0';i++){
        if(st.empty()){
            if (s[i]!=')'&&s[i]!=']'&&s[i]!='}') {
                st.push(s[i]);
            }else{
                return false;
            }
        }else{
            switch (s[i]){
                case '(':
                case '[':
                case '{':
                    st.push(s[i]);
                    break;
                case ')':
                    if(st.top()=='('){
                        st.pop();
                    }else{
                        return false;
                    }
                    break;
                case ']':
                    if(st.top()=='['){
                        st.pop();
                    }else{
                        return false;
                    }
                    break;
                case '}':
                    if(st.top()=='{'){
                        st.pop();
                    }else{
                        return false;
                    }
                    break;
                default:
                    break;
            }
        }
        
    }
    if(st.empty()){
        return true;
    }
    return false;
}
};
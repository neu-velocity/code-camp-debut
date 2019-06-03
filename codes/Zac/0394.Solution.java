class Solution {
    public String decodeString(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        int time = 0;
        StringBuilder curr = new StringBuilder();
        Stack<Integer> timeStack = new Stack();
        Stack<StringBuilder> strStack = new Stack();
        strStack.push(curr);
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                time *= 10;
                time += c - '0';
            } else if (c == '[') {
                timeStack.push(time);
                strStack.push(curr);
                curr = new StringBuilder();
                time = 0;
            } else if (c == ']') {
                int t = timeStack.pop();
                StringBuilder sb = strStack.pop();
                while (t-- > 0) {
                    sb.append(curr);
                }
                curr = sb;
            } else {
                curr.append(c);
            }
        }
        return strStack.pop().toString();
    }
}
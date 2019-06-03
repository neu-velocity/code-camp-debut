class Solution {
    public String decodeString(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }

        int time = 0;
        StringBuilder sb = new StringBuilder();
        Stack<Integer> timeStack = new Stack();
        Stack<StringBuilder> strStack = new Stack();

        strStack.push(sb);
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                time *= 10;
                time += c - '0';
            } else if (c == '[') {
                timeStack.push(time);
                strStack.push(sb);
                sb = new StringBuilder();
                time = 0;
            } else if (c == ']') {
                int t = timeStack.pop();
                StringBuilder pre = strStack.pop();
                while (t-- > 0) {
                    pre.append(sb);
                }
                sb = pre;
            } else {
                sb.append(c);
            }
        }
        return strStack.pop().toString();
    }
}
class Solution {
    public boolean isValid(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }
        Stack<Character> stack = new Stack();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty() || stack.pop() != '(') {
                    return false;
                }
            } else if (c == ']') {
                if (stack.isEmpty() || stack.pop() != '[') {
                    return false;
                }
            } else if (c == '}') {
                if (stack.isEmpty() || stack.pop() != '{') {
                    return false;
                }
            } else {
                return false;
            }
        }
        return stack.isEmpty();
    }
}
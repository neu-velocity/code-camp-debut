class Solution {
    public boolean isValid(String s) {
        char[] list = s.toCharArray();
        Stack<Character> checkStack = new Stack<>();
        int length = list.length;
        for (int i = 0; i < length; i++) {
            if (list[i] == '(') checkStack.push(list[i]);
            else if (list[i] == '{') checkStack.push(list[i]);
            else if (list[i] == '[') checkStack.push(list[i]);
            else if (list[i] == ')') {
                if (checkStack.isEmpty()) return false;
                if (checkStack.pop() != '(') return false;
            }
            else if (list[i] == ']') {
                if (checkStack.isEmpty()) return false;
                if (checkStack.pop() != '[') return false;
            }
            else if (list[i] == '}') {
                if (checkStack.isEmpty()) return false;
                if (checkStack.pop() != '{') return false;
            }
        }
        if (checkStack.isEmpty()) return true;
        else return false;
    }
}
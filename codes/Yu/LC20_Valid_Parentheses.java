import java.util.Stack;

class Solution {
	public boolean isValid(String s) {
		if (s.isEmpty()) // ""
			return true;
		else if ((s.charAt(0) != '(' && s.charAt(0) != '{' && s.charAt(0) != '[') || s.length() % 2 == 1) // ")" or odd length
			return false;

		Stack<Character> stack = new Stack<>();
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (c == '(' || c == '{' || c == '[')
				stack.push(c);
			else {

				switch (c) {
				case ')':
					if (stack.pop() == '(')
						break;
					else
						return false;
				case '}':
					if (stack.pop() == '{')
						break;
					else
						return false;
				case ']':
					if (stack.pop() == '[')
						break;
					else
						return false;
				default:
					return false;
				}
			}
		}
		return stack.isEmpty() ? true : false;
	}
}
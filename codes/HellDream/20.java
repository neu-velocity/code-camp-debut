class Solution {
    public boolean isValid(String s) {
        if(s==null || s.equals("")) return true;
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map  =new HashMap<>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c == '('||c == '['||c=='{'){
                stack.push(c);
            }else{
                if(!stack.isEmpty()&&stack.peek()==map.get(c)){
                    stack.pop();
                }else{
                    return false;
                }
            }
        }
        if(stack.isEmpty()) return true;
        return false;
    }
}
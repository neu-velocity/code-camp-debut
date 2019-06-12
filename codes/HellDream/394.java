class Solution {
    public String decodeString(String s) {
        Stack<Integer> numStack  =new Stack<>();
        Stack<String> sStack = new Stack<>();
        StringBuilder sb =new StringBuilder();
        int num = 0;
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(Character.isDigit(c)){
                num = c - '0';
                while(i+1<s.length()&& Character.isDigit(s.charAt(i+1))){
                    num  = num*10 + s.charAt(i+1)-'0';
                    i++;
                }
                numStack.push(num);
                num = 0;
            }else if(c == '['){
                sStack.push(sb.toString());
                sb = new StringBuilder();
            }else if(c ==']'){
                int times = numStack.pop();
                String sInStack = sStack.pop();
                StringBuilder tmp = new StringBuilder(sInStack);
                for(int t=0;t<times;t++){
                    tmp.append(sb);
                }
                sb  = tmp;
            }else{
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
class Solution:
    def isValid(self, s: str) -> bool:
        input_list = list(s)
        record_left = []

        for i in input_list:
            if  i in ['(', '[', '{']:
                record_left.append(i)
            
            else:

                if len(record_left) > 0:
                    if i == ')' and record_left[-1] != '(' :
                        return False
                    if i == '}' and record_left[-1] != '{':
                        return False
                    if i == ']' and record_left[-1] != '[':
                        return False

                else:
                    return False
                
                record_left.pop()
        
        
        return len(record_left) == 0
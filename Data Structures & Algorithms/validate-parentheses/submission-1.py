class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if stack !=[] and ( (stack[-1] == '(' and s[i] == ')') or (stack[-1] == '[' and s[i] == ']') or (stack[-1] == '{' and s[i] == '}')):
                stack.pop()
                continue
            else:
                stack.append(s[i])
        
        return stack == []
            

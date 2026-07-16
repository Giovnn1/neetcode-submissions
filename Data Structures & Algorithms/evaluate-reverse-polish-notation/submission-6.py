class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-' , '*', '/'}
        st = [tokens[0]]
        
        for ch in tokens[1:]:
            if ch in ops:
                res = int(eval(st[-2] + ch + st[-1]))
                st.pop()
                st.pop()
                st.append(str(res))
            else:
                st.append(ch)
        return int(st[0])
        
         


        
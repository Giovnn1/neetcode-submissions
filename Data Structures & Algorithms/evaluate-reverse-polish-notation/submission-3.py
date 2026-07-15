class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        ops = ('+', '-', '*', '/')
        st = []
        for i in range(len(tokens)):
            new = tokens[i]
            st.append(new)
            if len(st) >= 3 and st[-1] in ops and st[-2] not in ops and st[-3] not in ops:
                pop_op = st.pop()
                pop_r = st.pop()
                pop_l = st.pop()
                #if pop_op == '/':
                #    pop_op = '//'
                expression = str(pop_l) + pop_op + str(pop_r)
                result = int(eval(expression))
                st.append(result)
            
        return st[0]


        
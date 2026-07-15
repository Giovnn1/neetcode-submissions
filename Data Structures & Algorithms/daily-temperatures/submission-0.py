class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        res = len(t) * [0]
        st = [(t[0], 0)]
        for i in range(1, len(t)):
            while st and t[i] > st[-1][0]:
                p = st.pop()
                res[p[1]] = i - p[1]
            st.append((t[i], i))
        return res




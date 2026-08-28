class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = word1, word2# if len(word1) >= len(word2) else word2, word1
        if len(w1) > len(w2):
            w1, w2 = w2, w1
        l1, l2 = len(w1), len(w2)

        N = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        #I want N[u][v] to contain the number of operations needed to turn w1[:u] in w[:v]
        N[0] = [v for v in range(l2 + 1)]
        for u in range(l1 + 1):
            N[u][0] = u
        
        for u in range(1, l1 + 1):
            for v in range(1, l2 + 1):
                check = 0 if w1[u-1] == w2[v-1] else 0
                if w1[u - 1] == w2[v - 1]:
                    N[u][v] = N[u-1][v-1]
                else:
                    N[u][v] = 1 + min(N[u-1][v], N[u][v-1], N[u-1][v-1])
        return N[-1][-1]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        window = [(-n, i) for i, n in enumerate(nums[ : k])]
        discard = {}
        heapq.heapify(window)
        #[m, ind] = window[0]
        #res = (len(nums) - k) * [0]
        res = []
        res.append(- window[0][0])
        
        for i in range(1, len(nums) - k + 1):
            if nums[i-1] == res[i-1]:
                heapq.heappop(window)
            else:
                discard[(-nums[i-1], i - 1)] = 1
            heapq.heappush(window, (-nums[i + k - 1], i + k -1))
            while window[0] in discard:
                heapq.heappop(window)
            res.append( -window[0][0])
        return res




class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        left, right = 0, len(h) - 1
        m = 0 
        while left < right:
            area = min(h[left], h[right]) * (right - left)
            m = max(m, area)
            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
        return m


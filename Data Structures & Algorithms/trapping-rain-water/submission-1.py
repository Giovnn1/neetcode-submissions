class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        l = len(h)
        if not h:
            return 0
        left, leftMax, right, rightMax = 0, h[0], l - 1, h[l - 1]
        tot = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(h[left], leftMax)
                tot += leftMax - h[left]
            else:
                right -= 1
                rightMax = max(h[right], rightMax)
                tot += rightMax - h[right]
        return tot






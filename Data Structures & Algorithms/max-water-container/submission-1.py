class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        wid = len(heights) - 1
        ans = min(heights[left],heights[right]) * wid
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else: right -= 1
            wid -= 1
            ans = max(ans, min(heights[left],heights[right]) * wid)
        return ans
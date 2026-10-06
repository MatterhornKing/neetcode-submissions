class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        left = 0
        right = l - 1
        wid = l - 1
        ans = min(heights[left], heights[right]) * wid
        while left < right:
            if heights[left] < heights[right]:
                while left < right:
                    left += 1
                    wid -= 1
                    if heights[left] > heights[left-1]:
                        break
                tem = min(heights[left], heights[right]) * wid
                ans = max(ans,tem)
            else:
                while left < right:
                    right -= 1
                    wid -= 1
                    if heights[right] > heights[right+1]:
                        break
                tem = min(heights[left], heights[right]) * wid
                ans = max(ans,tem)
        return ans

        
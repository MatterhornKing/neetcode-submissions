class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        ans = 0
        while height[left] == 0:
            left += 1
            right = left + 1
            if left >= len(height) - 2:
                return ans
        while right < len(height):
            lb = height[left]
            rb = height[right]
            tem = 0
            while lb > rb and right < len(height):
                tem = tem + (lb - rb)
                right += 1
                if right < len(height):
                    rb = height[right]
                
            if right == len(height):
                break
            ans = ans + tem
            left = right
            right = left + 1
        
        ###reverse
        maxi = left
        if maxi >= len(height) - 2:
            return ans
        right = len(height) - 1
        left = right - 1
        while height[right] == 0:
            right -= 1
            left = right - 1

        while left > maxi:
            lb = height[left]
            rb = height[right]
            tem = 0
            while rb > lb and left > maxi:
                tem = tem + (rb - lb)
                left -= 1
                if left > maxi:
                    lb = height[left]
            if left == maxi:
                ans = ans + tem
                break
            ans = ans + tem
            right = left
            left = right - 1

        return ans
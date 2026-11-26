class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        i = l // 2
        left = 0
        right = l-1
        while left <= i <= right:
            if nums[i] == target:
                return i
            if nums[i] > target:
                right =  i - 1
                i = (right + left) // 2
            else:
                left = i + 1
                i = (right + left) // 2
        return -1
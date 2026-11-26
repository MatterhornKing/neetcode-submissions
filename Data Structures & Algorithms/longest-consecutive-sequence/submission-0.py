class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        maxi = 0

        for num in nums:
            if num - 1 in seen:
                continue
            i = 0
            while num + i in seen:
                i += 1
            if i > maxi:
                maxi = i
        
        return maxi
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pro = 1
        for num in nums:
            ans.append(pro)
            pro *= num
        pro2 = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= pro2
            pro2 *= nums[i]

        return ans
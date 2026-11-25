class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        max2 = []
        for i, n in enumerate(nums):
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        #count.items() # dict_items([(1,3), (2,5)]) view object
        #for num, freq in count.items():
        
        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])
        
        #bucket = [[] for _ in range(len(nums)+ 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        


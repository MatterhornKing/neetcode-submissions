class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = (sum(piles) + h - 1)// h 
        right = max(piles) 

        while left < right:
            mid = (left + right) // 2
            time = 0
            for num in piles:
                time += (num + mid - 1) // mid

            if time > h:
                left = mid + 1
            else:
                right = mid
        return right


        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for i in t:
            if i in count:
                count[i] -= 1
            else:
                return False
        
        return all(i==0 for i in count.values())
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        maxl = 0
        left = 0

        for right, char in enumerate(s):
            if char in sub and sub[char] >= left:
                left = sub[char] + 1
                
            sub[char] = right
            if right - left + 1 > maxl:
                    maxl = right - left + 1    
        return maxl
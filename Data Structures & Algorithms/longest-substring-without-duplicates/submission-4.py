class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        maxl = 0
        l = 0
        left = 0
        for i,char in enumerate(s):
            if char not in sub or sub[char] < left:
                sub[char] = i
                l += 1
            else:
                if l > maxl:
                    maxl = l
                left = sub[char] + 1
                l = i - left + 1
                sub[char] = i
            if l > maxl:
                    maxl = l
        return maxl

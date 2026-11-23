class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for j in t:
            if j in dic:
                dic[j] -= 1
                if dic[j] < 0:
                    return False
            else:
                return False
        
        for d in dic:
            if dic[d] != 0:
                return False
        return True
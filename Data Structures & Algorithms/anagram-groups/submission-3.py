class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)-ord("a")] += 1
            key = tuple(count)
            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]
        
        return list(group.values())
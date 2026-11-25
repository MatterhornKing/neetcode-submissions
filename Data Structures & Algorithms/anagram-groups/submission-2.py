class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in range(len(strs)):
            count = [0] * 26
            for s in strs[i]:
                count[ord(s)-ord("a")] += 1
            key = tuple(count)
            if key in group:
                group[key].append(i)
            else:
                group[key] = [i]
        ans = []
        for value in group.values():
            ans_sub = []
            for j in value:
                ans_sub.append(strs[j])
            ans.append(ans_sub)
        return ans
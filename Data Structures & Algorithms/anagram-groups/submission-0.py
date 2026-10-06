class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        count = {}
        
        for s in strs:
            key = 26 * [0]
            for char in s:
                key[ord(char) - ord('a')] += 1
            tup = tuple(key)
            if tup in count:
                count[tup].append(s)
            else:
                count[tup] = [s]

        return list(count.values())
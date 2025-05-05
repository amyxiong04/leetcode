class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list) # automatically creates a new list when a key is first seen
        for s in strs:
            key = tuple(sorted(s)) # use sorted string as key
            anagram[key].append(s)
        return list(anagram.values())
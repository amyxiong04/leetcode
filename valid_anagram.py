class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        for char in s:
            s_list.append(char)
        for char in t:
            t_list.append(char)
        s_list.sort()
        t_list.sort()
        if s_list == t_list:
            return True
        return False
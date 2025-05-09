class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        # if char is alphanumeric, convert to lowercase and add to cleaned
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        mid = len(cleaned) // 2
        left = 0
        right = len(cleaned) - 1

        for i in range(mid):
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1, t1 = {}, {}
        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 0)
            t1[t[i]] = 1 + t1.get(t[i], 0)

        for c in s1:
            if s1[c] != t1.get(c, 0):
                return False

        return True
    
# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

s = "anagram"
t = "nagaram"
solution = Solution()
result = solution.isAnagram(s, t)
print(result) 
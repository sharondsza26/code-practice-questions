class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapOpenClose = { ")" : "(",
                         "]" : "[",
                         "}" : "{" }

        for i in s:
            print(i, "///")
            if i in mapOpenClose:
                if stack and stack[-1] == mapOpenClose[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False

s = "()"
solution = Solution()
result = solution.isValid(s)
print(result) 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        
        for i in range(len(strs[0])) :
            for s in strs :
                if i == len(s) or s[i]!= strs[0][i]:
                    return res
            res += strs[0][i]
        return res
       
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
     
strs = ["flower","flow","flight"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result) 
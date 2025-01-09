from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        res = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
result = solution.maxArea(height)
print(result) 
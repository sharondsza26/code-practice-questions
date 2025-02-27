from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (right + left) // 2
            # print(mid, "mid")
            # print(left,right)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

    
nums = [3,4,5,1,2]
solution = Solution()
result = solution.findMin(nums)
print(result) 
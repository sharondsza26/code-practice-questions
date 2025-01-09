from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            print(answer, i, postfix)
            answer[i] *= postfix
            postfix *= nums[i]
            print(postfix, i)
        return answer
    
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

nums = [1,2,3,4]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result) 
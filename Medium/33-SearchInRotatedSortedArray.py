from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1


        while left <= right :
            mid = left + (right - left) //2
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    # move right
                    left = mid + 1
                else:
                    # move left
                    right = mid - 1

            else:
                if target < nums[mid] or target > nums[right]:
                    # move left
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
    
nums = [4,5,6,7,0,1,2]
target = 0
solution = Solution()
result = solution.search(nums, target)
print(result)   
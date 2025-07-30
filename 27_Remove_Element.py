from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Example usage
# Input list and value to remove
nums = [3, 2, 2, 3,9,8,7]
val = 3

# Call the method
sol = Solution()
k = sol.removeElement(nums, val)

# Output the results
print("New length (k):", k)
print("Modified list (first k elements):", nums[:k])
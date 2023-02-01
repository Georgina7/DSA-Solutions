## Question
# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. 
# If there are no target indices, return an empty list. The returned list must be sorted in increasing order. 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i], target <= 100

## My Solution
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_arr = sorted(nums)
        answer = []
        for i in range(len(sorted_arr)):
            if sorted_arr[i] == target:
                answer.append(i)
        return answer

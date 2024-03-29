## Question
# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

## Example 1
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

## Example 2
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

## Constraints
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

## Solution 1 - Time Complexity[O(nLogn)], Space Complexity[O(1)] 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        count = 0

        while(start < end):
            sum = nums[start] + nums[end]
            if sum == k:
                start += 1
                end -= 1
                count += 1
            elif sum > k:
                end -= 1
            else:
                start += 1
        return count
    
## Solution 2 - Time Complexity[O(n)], Space Complexity[O(n)]
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = {}
        for num in nums:
            pairs[num] = pairs.get(num, 0) + 1

        count = 0
        for key in pairs.keys():
            if k - key in pairs:
                if k - key == key:
                    count += (pairs[key] // 2)
                else:
                    count += min(pairs[key], pairs[k - key])
                    pairs[key] = 0
        return count

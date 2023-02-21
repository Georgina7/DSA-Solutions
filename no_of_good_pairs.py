## Question
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j. 

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

## My Solution -  O(n!)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_length = len(nums)
        count = 0
        for i in range(nums_length):
            for j in range(i + 1, nums_length):
                if nums[i] == nums[j]:
                    count += 1
        
        return count
      
## Effecient solution - O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:            
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res

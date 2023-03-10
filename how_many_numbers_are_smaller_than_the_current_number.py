## Question
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array. 

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Constraints:

# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

## Solution 1 - O(n**2)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if not count.get(nums[i]):
                for j in range(len(nums)):                
                    if nums[j] < nums[i]:
                        count[nums[i]] = count.get(nums[i], 0) + 1
            count[nums[i]] = count.get(nums[i], 0)

        answer = []
        for val in nums:
            answer.append(count[val])
        return answer
     
## Solution 2 - O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        nums_sorted = sorted(nums)
        smallerNum = -1
        smallerCount = 0
        for val in nums_sorted:
            if smallerNum < val:
                count[val] = count.get(val, 0) + smallerCount                
            smallerNum = val
            smallerCount +=1

        answer = []
        for val in nums:
            answer.append(count[val])

        return answer

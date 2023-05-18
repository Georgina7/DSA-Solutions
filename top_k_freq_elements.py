## Question
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Example
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

## Constraints
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

## My Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq_dict = sorted(freq_dict.items(), key=lambda x:x[1],            reverse=True)
        answer = []
        for i in range(k):
            answer.append(freq_dict[i][0])
        return answer
        

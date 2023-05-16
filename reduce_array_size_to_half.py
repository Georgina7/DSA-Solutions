##  Question
# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.

## Example
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

## Constraints
# 2 <= arr.length <= 105
# arr.length is even.
# 1 <= arr[i] <= 105

## My Solution
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_dict = {}
        
        for val in arr:
            freq_dict[val] = freq_dict.get(val, 0) + 1

        freq_list = list(freq_dict.values())
        freq_list.sort(reverse=True)
        set_size = 0
        answer = 0

        for val in freq_list:
            set_size += val
            answer += 1
            if set_size >= len(arr)//2:
                return answer
                  


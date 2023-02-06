## Question
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

## Selection Sort - O(n**2)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            smallest = min(nums[i:])
            index = nums[i:].index(smallest) + i
            nums[i], nums[index] = nums[index], nums[i]
            
## Quick Sort - O(nlog(n))
class Solution:
    # Function to find the partition position
    def partition(self, arr, low, high):
        # Choose the rightmost element as pivot
        pivot = arr[high]

        # Pointer for greater element
        i = low - 1

        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            if arr[j] <= pivot:
                # If element is smaller than pivot, swap it with the greater element pointed by i
                i += 1

                # Swapping element at i with element at j
                (arr[i], arr[j]) = (arr[j], arr[i])
        
        # Swap the pivot element with the greater element specified by i
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1 ])

        # Return the position from where partition is done
        return i + 1

    # Function to perform quick sort
    def quick_sort(self, arr, low, high):
        if low < high:
            # Find pivot element such that
            # Element smaller than pivot are on the left
            # Element greater than pivot are on the right
            pi = self.partition(arr, low, high)
            # Recursive call on the left of pivot
            self.quick_sort(arr, low, pi - 1)
            # Recursive call on the right of pivot
            self.quick_sort(arr, pi + 1, high)
            
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        

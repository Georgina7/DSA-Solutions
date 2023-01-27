## Question
# Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

## My Solution 
class Solution: 
    def select(self, arr, i):
        smallest_pos = i
        for i in range(i, len(arr)):
            if arr[i] < arr[smallest_pos]:
                smallest_pos = i
        return smallest_pos
    
    def selectionSort(self, arr,n):
        for i in range(n):
            pos = self.select(arr, i)
            arr[i], arr[pos] = arr[pos], arr[i]
        return arr

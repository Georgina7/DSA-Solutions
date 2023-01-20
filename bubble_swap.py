## Question
# Consider the following version of Bubble Sort:

# for (int i = 0; i < n; i++) {
    
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#         }
#     }
    
# }

# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

# Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
# First Element: firstElement, where  is the first element in the sorted array.
# Last Element: lastElement, where  is the last element in the sorted array.

## My Solution
def countSwaps(a):
    # Write your code here
    swap = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap += 1
    print('Array is sorted in {} swaps.'.format(swap))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[len(a) - 1]))

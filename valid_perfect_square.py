## Question
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

## Example 1:
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

## Example 2:
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer. 

## Constraints:
# 1 <= num <= 231 - 1

## My Solution 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        record = {}
        for i in range((num + 1)//2): 
            record[(i+1)**2] = record.get((i+1)**2, 1)
            
        if record.get(num) == None:
            return False
        return True
      
## Efficient Solution
# Newton's Solution
    def NewtonMethod(self, num):
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num

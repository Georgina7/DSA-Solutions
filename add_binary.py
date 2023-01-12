## Question:
# Given two binary strings a and b, return their sum as a binary string. 

## Example 1:
# Input: a = "11", b = "1"
# Output: "100"

## Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 
## Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        ## My Solution
        if len(a) > len(b):
            b = ('0' * (len(a) - len(b))) + b
        else:
            a = ('0' * (len(b) - len(a))) + a

        carry = '0'
        ans = ''
        for i in reversed(range(len(a))):
            if a[i] == b[i] and a[i] == '1':
                if carry == '0':
                    ans = '0' + ans
                else:
                    ans = '1' + ans
                carry = '1'                
            elif a[i] == b[i] and a[i] == '0':
                if carry == '1':
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                carry = '0'
            else:
                if carry == '1':
                    ans = '0' + ans
                    carry = '1'
                else:
                    ans = '1' + ans
        
        if carry == '1':
            ans = '1' + ans
        
        return ans

        ## Efficient Solution
        sum = int(a, 2) + int(b, 2)
        return str(bin(sum))[2:]
            

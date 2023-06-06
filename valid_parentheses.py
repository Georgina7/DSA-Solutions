## Question
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

## Examples
# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true


## Constraints
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

## Hints
# Use a stack of characters.
# When you encounter an opening bracket, push it to the top of the stack.
# When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

## My Solution
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        for bracket in s:
            if (brackets.get(bracket)):
                stack.insert(0, [bracket, brackets[bracket]])
            else:
                if len(stack)  > 0 and stack[0][1] == bracket:
                    stack.pop(0)
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False

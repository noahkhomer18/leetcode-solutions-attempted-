# Palindrome Number

**Problem Number:** 9  
**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/palindrome-number/

## Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

## Examples

### Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

### Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Constraints
- -2^31 <= x <= 2^31 - 1

## Follow-up
Could you solve it without converting the integer to a string?

## Solutions
See the `solutions/` folder for my attempted solutions.

## Notes
- [x] First attempt - Reverse half the number, avoid string conversion
- [x] Optimized solution - O(log10(n)) time, O(1) space
- [x] Edge cases handled - Negatives, trailing zeros

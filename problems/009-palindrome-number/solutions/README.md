# Palindrome Number - Solutions

## Solution 1: Reverse Half of the Number (No Strings)
**Time Complexity:** O(log10(n))  
**Space Complexity:** O(1)

### Approach
- Negative numbers are not palindromes.
- Numbers ending with 0 are not palindromes unless the number is 0.
- Reverse only the last half of the digits and compare with the remaining first half.
  - When the reversed half becomes greater than or equal to the remaining half, stop.

### Code
```python
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return x == reversed_num or x == reversed_num // 10
```

### Why This Works
- For even digits: at termination, `x == reversed_num`.
- For odd digits: middle digit is ignored by `reversed_num // 10`, so compare `x == reversed_num // 10`.

### Edge Cases
- `x < 0` → False
- `x` ends with 0 but `x != 0` → False
- `0` → True

## Notes
- Avoids converting `x` to a string.
- Only processes half of the digits, improving efficiency.

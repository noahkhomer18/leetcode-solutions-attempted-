# Reverse Integer - Solutions

## Solution 1: String Reversal (Optimal)
**Time Complexity:** O(log n)  
**Space Complexity:** O(log n)

### Approach
Convert the integer to string, reverse it, then convert back to integer while handling overflow constraints.

### Code
```python
class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = int(str(x_abs)[::-1]) * sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
```

### Explanation
1. **Handle Sign**: Store the sign of the original number
2. **Work with Absolute Value**: Convert to positive to simplify reversal
3. **String Reversal**: Convert to string, reverse using slice notation `[::-1]`
4. **Convert Back**: Convert back to integer and apply original sign
5. **Overflow Check**: Verify the result is within 32-bit integer range
6. **Return Result**: Return 0 if overflow, otherwise return reversed number

### Key Insights
- **String Reversal**: `str(x_abs)[::-1]` efficiently reverses the string
- **Overflow Detection**: Check against `INT_MIN` (-2^31) and `INT_MAX` (2^31 - 1)
- **Sign Preservation**: Handle negative numbers by storing and reapplying the sign
- **Edge Case**: Return 0 for any overflow situation

### Why This Works
- **Simple and Readable**: Easy to understand and implement
- **Handles All Cases**: Works for positive, negative, and zero inputs
- **Overflow Safe**: Properly detects and handles 32-bit integer overflow
- **Efficient**: O(log n) time complexity due to string operations

## Alternative Approach: Mathematical
While the string approach is simpler, a mathematical approach would:
1. Extract digits using modulo and division
2. Build reversed number digit by digit
3. Check for overflow during construction

However, the string approach is more intuitive and equally efficient for this problem.

## Test Results
- ✅ Example 1: 123 → 321
- ✅ Example 2: -123 → -321
- ✅ Example 3: 120 → 21
- ✅ Zero: 0 → 0
- ✅ Overflow: 1534236469 → 0
- ✅ Min Int: -2147483648 → 0

## Notes
- This solution handles the constraint of not storing 64-bit integers
- The string conversion approach is clean and readable
- Overflow detection is crucial for this problem's constraints

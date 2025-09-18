# String to Integer (atoi) - Solutions

## Solution 1: String Parsing with Overflow Detection (Optimal)
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

### Approach
Parse the string step by step following the algorithm requirements: skip whitespace, determine sign, convert digits, and handle overflow.

### Code
```python
class Solution:
    def myAtoi(self, s):
        i, n = 0, len(s)
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Determine sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits with overflow detection
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before adding the digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return sign * num
```

### Explanation

#### Step 1: Skip Leading Whitespace
```python
while i < n and s[i] == ' ':
    i += 1
```
- Move pointer past any leading spaces
- Only spaces are considered whitespace (not tabs, newlines, etc.)

#### Step 2: Determine Sign
```python
sign = 1
if i < n and (s[i] == '+' or s[i] == '-'):
    if s[i] == '-':
        sign = -1
    i += 1
```
- Default to positive sign
- Check for explicit '+' or '-' character
- Move pointer past the sign character

#### Step 3: Convert Digits with Overflow Detection
```python
num = 0
while i < n and s[i].isdigit():
    digit = int(s[i])
    if num > (INT_MAX - digit) // 10:
        return INT_MAX if sign == 1 else INT_MIN
    num = num * 10 + digit
    i += 1
```
- Build number digit by digit
- **Key Insight**: Check overflow before adding the digit
- Formula: `num > (INT_MAX - digit) // 10` prevents overflow
- Stop at first non-digit character

### Key Insights

1. **Overflow Prevention**: Check `num > (INT_MAX - digit) // 10` before adding
   - This ensures `num * 10 + digit` won't exceed `INT_MAX`
   - Equivalent to: `num * 10 + digit > INT_MAX`

2. **Early Termination**: Stop at first non-digit character
   - Handles cases like "1337c0d3" → 1337

3. **Sign Handling**: Apply sign at the end
   - More efficient than tracking sign during digit conversion

4. **Edge Cases**:
   - Empty string or only whitespace → 0
   - No digits found → 0
   - Overflow → clamp to INT_MAX/INT_MIN

### Why This Works
- **Follows Algorithm**: Implements the exact 4-step process described
- **Overflow Safe**: Prevents integer overflow during conversion
- **Efficient**: Single pass through the string
- **Robust**: Handles all edge cases mentioned in examples

## Test Results
- ✅ Example 1: "42" → 42
- ✅ Example 2: "   -042" → -42
- ✅ Example 3: "1337c0d3" → 1337
- ✅ Example 4: "0-1" → 0
- ✅ Example 5: "words and 987" → 0
- ✅ Positive with spaces: "   +123" → 123
- ✅ Overflow: "2147483648" → 2147483647
- ✅ Underflow: "-2147483649" → -2147483648

## Notes
- This solution perfectly implements the atoi function as specified
- The overflow detection formula is crucial for handling large numbers
- Single pass algorithm makes it very efficient

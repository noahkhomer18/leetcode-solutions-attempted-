# Solution Explanation

## Approach: Hash Map with Subtraction Logic

This solution uses a hash map to store symbol values and processes the string from right to left.

### Algorithm:
1. **Create hash map:** Map each Roman symbol to its value
2. **Process right to left:** Iterate through the string in reverse order
3. **Subtraction logic:** If current value < previous value, subtract it
4. **Addition logic:** Otherwise, add the current value to total
5. **Update previous:** Keep track of the previous value for comparison

### Why This Works:
- Processing from right to left handles subtraction cases naturally
- If current symbol value < previous symbol value, it's a subtraction case (IV, IX, XL, XC, CD, CM)
- Otherwise, it's a normal addition case
- The algorithm correctly handles all Roman numeral rules

### Time Complexity: O(n)
- Single pass through the string
- Hash map lookup is O(1)

### Space Complexity: O(1)
- Constant space for the hash map (7 symbols)
- Only a few variables for tracking

## Test Cases:
- `"III"` → `3`
- `"LVIII"` → `58`
- `"MCMXCIV"` → `1994`
- `"IV"` → `4`
- `"IX"` → `9`

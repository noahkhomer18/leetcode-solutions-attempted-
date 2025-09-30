# Solution Explanation

## Approach: Greedy Algorithm

This solution uses a greedy approach to convert integers to Roman numerals.

### Algorithm:
1. **Create arrays:** Values and corresponding symbols in descending order
2. **Include subtractive forms:** 900 (CM), 400 (CD), 90 (XC), 40 (XL), 9 (IX), 4 (IV)
3. **Greedy selection:** For each value, repeatedly subtract it from the number
4. **Append symbols:** Add the corresponding symbol to the result string
5. **Continue:** Move to the next smaller value until number becomes 0

### Why This Works:
- Roman numerals follow a greedy pattern: always use the largest possible symbol
- Including subtractive forms in the values array simplifies the logic
- Processing values in descending order ensures correct conversion
- The algorithm handles all edge cases (4, 9, 40, 90, 400, 900) automatically

### Time Complexity: O(1)
- Constant time since we have a fixed number of Roman symbols (13 symbols)
- Each symbol is processed at most once

### Space Complexity: O(1)
- Constant space for the values and symbols arrays
- Result string length is bounded by the input (max 3999)

## Test Cases:
- `3749` → `"MMMDCCXLIX"`
- `58` → `"LVIII"`
- `1994` → `"MCMXCIV"`
- `3` → `"III"`

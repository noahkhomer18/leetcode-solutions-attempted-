# Zigzag Conversion - Solutions

## Solution 1: Row-by-Row Approach (Optimal)
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

### Approach
Instead of simulating the zigzag pattern, we can directly place characters in their correct rows by tracking the current row and direction.

### Code
```python
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        index, step = 0, 1
        
        for char in s:
            rows[index] += char
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
                
            index += step
            
        return ''.join(rows)
```

### Explanation
1. Create an array of strings, one for each row
2. Use `index` to track current row and `step` to track direction
3. For each character:
   - Add it to the current row
   - Update direction when reaching top (0) or bottom (numRows-1)
   - Move to next row based on current direction
4. Join all rows to get the final result

### Key Insights
- **Direction Change**: When `index == 0`, we're at the top, so go down (`step = 1`)
- **Direction Change**: When `index == numRows - 1`, we're at the bottom, so go up (`step = -1`)
- **Edge Cases**: If `numRows == 1` or `numRows >= len(s)`, return original string

### Why This Works
- We simulate the zigzag movement without actually creating the 2D pattern
- Each character is placed directly in its final position
- The step direction automatically handles the zigzag movement
- Time complexity is O(n) because we visit each character exactly once

## Test Results
- ✅ Example 1: "PAYPALISHIRING", 3 rows → "PAHNAPLSIIGYIR"
- ✅ Example 2: "PAYPALISHIRING", 4 rows → "PINALSIGYAHRPI"
- ✅ Example 3: "A", 1 row → "A"
- ✅ Single row: "AB", 1 row → "AB"
- ✅ Two rows: "ABC", 2 rows → "ACB"

## Notes
- This approach is more efficient than simulating the actual zigzag pattern
- Handles all edge cases elegantly
- The direction logic is the key to the solution's elegance

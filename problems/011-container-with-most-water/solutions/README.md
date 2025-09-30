# Solution Explanation

## Approach: Two Pointers

This solution uses the two pointers technique to efficiently find the maximum area.

### Algorithm:
1. **Initialize pointers:** Start with `left = 0` and `right = len(height) - 1`
2. **Calculate area:** `area = width * min(height[left], height[right])`
3. **Update maximum:** Keep track of the maximum area found
4. **Move pointer:** Move the pointer pointing to the shorter line inward
5. **Repeat:** Continue until pointers meet

### Why This Works:
- The area is limited by the shorter of the two lines
- Moving the pointer at the taller line inward will never increase the area
- Moving the pointer at the shorter line might find a better area
- This guarantees we don't miss the optimal solution

### Time Complexity: O(n)
- Single pass through the array
- Each element is visited at most once

### Space Complexity: O(1)
- Only using two pointers and a few variables
- No additional data structures needed

## Test Cases:
- `[1,8,6,2,5,4,8,3,7]` → `49`
- `[1,1]` → `1`
- `[1,2,1]` → `2`

# Two Sum - Solutions

## Solution 1: Hash Map (Optimal)
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

### Approach
Use a hash map to store numbers and their indices as we iterate through the array. For each number, calculate the complement (target - current number) and check if it exists in the hash map.

### Code
```python
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
```

### Explanation
1. Create an empty hash map to store number-index pairs
2. Iterate through the array with index
3. For each number, calculate its complement (target - current number)
4. If complement exists in hash map, return the indices
5. Otherwise, store current number and its index in hash map

### Why This Works
- We only need one pass through the array
- Hash map lookup is O(1) average case
- We store each number only once, so space is O(n)
- Guaranteed to find solution since problem states exactly one solution exists

## Test Results
- ✅ Example 1: [2,7,11,15], target=9 → [0,1]
- ✅ Example 2: [3,2,4], target=6 → [1,2]  
- ✅ Example 3: [3,3], target=6 → [0,1]

## Notes
- This solution answers the follow-up question: O(n) time complexity is better than O(n²)
- Handles edge cases like duplicate numbers correctly
- Returns indices in the order they appear in the original array
